from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.user import RepositoryUser
from src.schemas.schemas import SimpleUser, User


router = APIRouter()


@router.post('/users', status_code=status.HTTP_201_CREATED, response_model=User)
def create_user(user: User, db: Session = Depends(get_db)):
    user_created = RepositoryUser(db).create(user)
    return user_created

@router.get('/users', response_model=List[User])
def listem_user(db: Session = Depends(get_db)):
    user = RepositoryUser(db).listem()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'Not found User')
    return user


@router.get('/users/{id}')
def search_user(id: int , db: Session = Depends(get_db)):
    user = RepositoryUser(db).search(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'Not found User with ID = {id}')
    return user


@router.put('/users/{id}', response_model=SimpleUser)
def update_user(id: int, user: User, db: Session = Depends(get_db)):
    RepositoryUser(db).edit(id, user)
    user.id = id
    return user


@router.delete('/users/{id}')
def remove_user(id: int, db: Session = Depends(get_db)):
    RepositoryUser(db).remove(id)
    return {'msg': 'Product deleted.'}