import time
from typing import Dict
import jwt
from decouple import config


JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


# Генерация токена 
def signJWT( user_id: str, login: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "login": login,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return  {"accessToken": token}

# Расшифровка токена
def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}