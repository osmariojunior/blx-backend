from fastapi import FastAPI, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositories.user import RepositoryUser
from src.schemas.schemas import Product, SimpleProduct, User
from src.infra.sqlalchemy.config.database import get_db, start_db
from src.infra.sqlalchemy.repositories.product import RepositoryProduct
from fastapi.middleware.cors import CORSMiddleware

start_db()

app = FastAPI()

# CORS

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# PRODUCTS

@app.post('/products', status_code=status.HTTP_201_CREATED, response_model=SimpleProduct)
def create_product(product: Product, db: Session = Depends(get_db)):
    product_created = RepositoryProduct(db).create(product)
    return product_created

@app.get('/products', status_code=status.HTTP_200_OK, response_model=List[Product])
def listem_product(db: Session = Depends(get_db)):
    product = RepositoryProduct(db).listem()
    return product

@app.put('/products/{id}', response_model=SimpleProduct)
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    RepositoryProduct(db).edit(id, product)
    product.id = id
    return product

@app.delete('/products/{id}')
def remove_product(id: int, db: Session = Depends(get_db)):
    RepositoryProduct(db).remove(id)
    return {'msg': 'Product deleted.'}


# USERS

@app.post('/users', status_code=status.HTTP_201_CREATED, response_model=User)
def create_user(user: User, db: Session = Depends(get_db)):
    user_created = RepositoryUser(db).create(user)
    return user_created

@app.get('/users', status_code=status.HTTP_200_OK, response_model=List[User])
def listem_user(db: Session = Depends(get_db)):
    user = RepositoryUser(db).listem()
    return user