from fastapi import FastAPI, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Product, SimpleProduct
from src.infra.sqlalchemy.config.database import get_db, start_db
from src.infra.sqlalchemy.repositories.product import RepositoryProduct

start_db()

app = FastAPI()


@app.post('/products', status_code=status.HTTP_201_CREATED, response_model=SimpleProduct)
def create_product(product: Product, db: Session = Depends(get_db)):
    product_created = RepositoryProduct(db).create(product)
    return product_created

@app.get('/products', status_code=status.HTTP_200_OK, response_model=List[Product])
def listem_product(db: Session = Depends(get_db)):
    product = RepositoryProduct(db).listem()
    return product
