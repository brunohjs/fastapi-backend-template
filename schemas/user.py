import pydantic


class UserBase(pydantic.BaseModel):
    email: pydantic.EmailStr
    full_name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        from_attributes = True
