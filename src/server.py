from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemas.schemas import Product
from src.infra.sqlalchemy.config.database import get_db, start_db
from src.infra.sqlalchemy.repositories.product import RepositoryProduct

start_db()

app = FastAPI()


@app.post('/products')
def create_product(product: Product, db: Session = Depends(get_db)):
    product_created = RepositoryProduct(db).create(product)
    return product_created

@app.get('/products')
def listem_product(db: Session = Depends(get_db)):
    product = RepositoryProduct(db).listem()
    return product