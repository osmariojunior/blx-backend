from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositoryProduct():
    def __init__(self, session: Session):
        self.session = session

    def create(self, product: schemas.Product):
        db_product = models.Product(name=product.name,
                                    details=product.details,
                                    price=product.price,
                                    available=product.available,
                                    user_id=product.user_id)
        self.session.add(db_product)
        self.session.commit()
        self.session.refresh(db_product)
        return db_product

    def listem(self):
        stmt = select(models.Product)
        products = self.session.execute(stmt).scalars().all()
        return products

    def edit(self, id: int, product: schemas.Product):
        update_stmt = update(models.Product).where(
            models.Product.id == id).values(name=product.name,
                                                    details=product.details,
                                                    price=product.price,
                                                    available=product.available)
   
        self.session.execute(update_stmt)
        self.session.commit()

    def remove(self, id: int):
        delete_stmt = delete(models.Product).where(
            models.Product.id == id)

        self.session.execute(delete_stmt)
        self.session.commit()