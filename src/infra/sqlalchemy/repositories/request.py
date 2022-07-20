from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.schemas.schemas import RequestsOrder
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
        request = self.session.execute(stmt).scalars().all()
        return request


    def listem_purchase_for_user_id(self, user_id: int):
        query = select(models.Request).where(models.Request.user_id == user_id)
        request = self.session.execute(query).scalars().all()
        return request

    
    def listem_sales_for_user_id(self,  user_id: int):
        query = select(models.Request, models.Product).join_from(models.Request, models.Product).where(models.Request.user_id == user_id)
        request = self.session.execute(query).scalars().all()
        return request


    def search(self, id: int) -> models.Request:
        query = select(models.Request).where(models.Request.id == id)
        request = self.session.execute(query).one()
        return request[0]


    def edit(self, id: int, request: schemas.RequestsOrder):
        update_stmt = update(models.Request).where(
            models.Request.id == id).values(amount=request.amount,
                                            adress_delivery=request.adress_delivery,
                                            type_delivery=request.type_delivery,
                                            comments=request.comments)
   
        self.session.execute(update_stmt)
        self.session.commit()

    def remove(self, id: int):
        delete_stmt = delete(models.Request).where(
            models.Request.id == id)

        self.session.execute(delete_stmt)
        self.session.commit()
