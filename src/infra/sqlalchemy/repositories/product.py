import imp
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositoryProduct():
    def __init__(self, db: Session):
        self.db = db

    def create(self, product: schemas.Product):
        db_product = models.Product(name=product.name,
                                    details=product.details,
                                    price=product.price,
                                    available=product.available)
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def listem(self):
        products = self.db.query(models.Product).all()
        return products

    def get(self):
        pass

    def remove(self):
        pass