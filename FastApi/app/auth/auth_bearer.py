from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from .auth_handler import decodeJWT


class JWTBearer(HTTPBearer):
    def __init__(self, individual_access: bool, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)
        self.individual_access = individual_access

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials): # Валидность токена
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            if self.individual_access: # Статус необходимости разделения доступа
                if self.verify_name(credentials.credentials, request):
                    raise HTTPException(status_code=403, detail="You don't have access to this data.")
            return credentials.credentials
        else: 
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

# Проверка валидности токена
    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False

        try:
            payload = decodeJWT(jwtoken)
        except:
            payload = None
        if payload :
            isTokenValid = True
        return isTokenValid

# Проверка разрешения доступа к данным для пользователя
    def verify_name(self ,jwtoken: str, request: Request) -> bool:
        isUserAccessAllowed = True
        payload = decodeJWT(jwtoken)
        user_id_from_responce = request.url.path.split('/')[-1]
        if payload['user_id']  == user_id_from_responce:
            isUserAccessAllowed = False
        return isUserAccessAllowed
        