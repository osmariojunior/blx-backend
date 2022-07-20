from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.user import RepositoryUser
from src.schemas.schemas import User


router = APIRouter()


@router.post('/users', status_code=status.HTTP_201_CREATED, response_model=User)
def create_user(user: User, db: Session = Depends(get_db)):
    user_created = RepositoryUser(db).create(user)
    return user_created

@router.get('/users', status_code=status.HTTP_200_OK, response_model=List[User])
def listem_user(db: Session = Depends(get_db)):
    user = RepositoryUser(db).listem()
    return user