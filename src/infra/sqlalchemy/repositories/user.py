from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositoryUser():
    def __init__(self, session: Session):
        self.session = session

    def create(self, user: schemas.User):
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


    def search(self, id: int):
        query = select(models.User).where(models.User.id == id)
        user = self.session.execute(query).first()
        return user


    def verify_phone(self, phone):
        query = select(models.User).where(models.User.phone == phone)
        user = self.session.execute(query).first()
        return user


    def edit(self, id: int, user: schemas.User):
        update_stmt = update(models.User).where(
            models.User.id == id).values(name=user.name,
                                            phone=user.phone,
                                            password=user.password)
   
        self.session.execute(update_stmt)
        self.session.commit()


    def remove(self, id: int):
        delete_stmt = delete(models.User).where(
            models.User.id == id)

        self.session.execute(delete_stmt)
        self.session.commit()