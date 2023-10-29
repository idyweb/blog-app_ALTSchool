from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field


# properties required during user creation
class UserCreate(BaseModel):
    firstname: str
    lastname: str
    username: str
    email: EmailStr
    password: str = Field(..., min_length=1)


class ShowUser(BaseModel):
    id: int
    firstname: str
    lastname: str
    username: str
    email: EmailStr

    class Config:  # tells pydantic to convert even non dict obj to json
        orm_mode = True


class UserLoginSchema(BaseModel):
    username: str = Field(...)
    password: str = Field(...)
