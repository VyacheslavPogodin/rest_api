
from pydantic import BaseModel, Field

class UserLoginSchema(BaseModel):
    login: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {"example": {'login':'Sidorov', 'password' :'1234'}
                    }