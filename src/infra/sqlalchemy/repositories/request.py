from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositoryRequest():
    def __init__(self, session: Session):
        self.session = session

    def create(self, request: schemas.RequestsOrder):
        db_request = models.Request(amount=request.amount,
                                    adress_delivery=request.adress_delivery,
                                    type_delivery=request.type_delivery,
                                    comments=request.comments,
                                    user_id=request.user_id,
                                    product_id=request.product_id)

        self.session.add(db_request)
        self.session.commit()
        self.session.refresh(db_request)
        return db_request

    def listem(self):
        stmt = select(models.Request)
        products = self.session.execute(stmt).scalars().all()
        return products


    def search(self, id: int):
        query = select(models.Request).where(models.Request.id == id)
        request = self.session.execute(query).first()
        return request


''' def edit(self, id: int, request: schemas.Request):
        update_stmt = update(models.Request).where(
            models.Request.id == id).values(name=request.name,
                                            details=request.details,
                                            price=request.price,
                                            available=request.available)
   
        self.session.execute(update_stmt)
        self.session.commit()

    def remove(self, id: int):
        delete_stmt = delete(models.Request).where(
            models.Request.id == id)

        self.session.execute(delete_stmt)
        self.session.commit()
'''