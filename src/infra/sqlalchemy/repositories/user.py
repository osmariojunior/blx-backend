from sqlalchemy import select
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositoryUser():
    def __init__(self, session: Session):
        self.session = session

    def create(self, user: schemas.Product):
        db_user = models.User(  name=user.name,
                                phone=user.phone,
                                password=user.password) 
        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return db_user

    def listem(self):
        stmt = select(models.User)
        user = self.session.execute(stmt).scalars().all()
        return user

    def get(self):
        pass

    def remove(self):
        pass