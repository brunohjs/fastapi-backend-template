import fastapi
from schemas.user import User
from schemas.user import UserCreate
from services import user_service


router = fastapi.APIRouter()


@router.post("/user", response_model=User)
async def create_new_user(user: UserCreate):
    return await user_service.create_user(user)


@router.get("/user/{user_id}", response_model=User)
async def read_user(user_id: int):
    user = await user_service.get_user(user_id)
    if not user:
        raise fastapi.HTTPException(status_code=404, detail="User not found")
    return user
