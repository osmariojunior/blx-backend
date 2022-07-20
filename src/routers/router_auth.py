from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.user import RepositoryUser
from src.schemas.schemas import SimpleUser, User
from src.infra.providers import hash_provider


router = APIRouter()


@router.post('/singup', status_code=status.HTTP_201_CREATED, response_model=User)
def singup(user: User, db: Session = Depends(get_db)):
    user_already_registered = RepositoryUser(db).verify_phone(user.phone)
    if user_already_registered:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= f'User already registered.')
    user.password = hash_provider.generate_hash(user.password)
    user_created = RepositoryUser(db).create(user)
    return user_created


@router.get('/users', response_model=List[User])
def listem_user(db: Session = Depends(get_db)):
    user = RepositoryUser(db).listem()
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
    return {'msg': 'User deleted.'}