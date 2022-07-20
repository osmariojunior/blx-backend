from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.product import RepositoryProduct
from src.schemas.schemas import Product, SimpleProduct


router = APIRouter()


@router.post('/products', status_code=status.HTTP_201_CREATED, response_model=SimpleProduct)
def create_product(product: Product, db: Session = Depends(get_db)):
    product_created = RepositoryProduct(db).create(product)
    return product_created

@router.get('/products', status_code=status.HTTP_200_OK, response_model=List[Product])
def listem_product(db: Session = Depends(get_db)):
    product = RepositoryProduct(db).listem()
    return product

@router.put('/products/{id}', response_model=SimpleProduct)
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    RepositoryProduct(db).edit(id, product)
    product.id = id
    return product

@router.delete('/products/{id}')
def remove_product(id: int, db: Session = Depends(get_db)):
    RepositoryProduct(db).remove(id)
    return {'msg': 'Product deleted.'}
