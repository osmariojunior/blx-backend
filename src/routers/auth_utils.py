from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import token_provider
from fastapi import Depends, HTTPException, status

from src.infra.sqlalchemy.repositories.user import RepositoryUser

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')


def get_user_logged(token: str = Depends(oauth2_schema), session: Session = Depends(get_db)):
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    try:
        phone = token_provider.verify_access_token(token)
    except JWTError:
        raise exception

    if not phone:
        raise exception
    user = RepositoryUser(session).verify_phone(phone)

    if not user:
        raise exception
    
    return user
