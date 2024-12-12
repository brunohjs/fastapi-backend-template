from sqlalchemy.orm import Session

from src.models.user import User


async def create_user_repo(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


async def get_user_repo(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
