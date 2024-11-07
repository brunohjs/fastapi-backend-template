from schemas.user import UserCreate
from models.user import User
from security import security
from repositories import user


async def create_user(user_in: UserCreate):
    hashed_password = security.hash_password(user_in.password)
    user_data = User(
        email=user_in.email,
        full_name=user_in.full_name,
        hashed_password=hashed_password
    )
    return await user.create_user_repo(user_data)


async def get_user(user_id: int):
    return await user.get_user_repo(user_id)
