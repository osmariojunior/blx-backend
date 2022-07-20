from pydantic import BaseModel
from typing import Optional, List


class SimpleProduct(BaseModel):
    id: Optional[int] = None
    name: str
    price: float
    available: bool

    class Config:
        orm_mode = True

class User(BaseModel):
    id: Optional[int] = None
    name: str
    phone: str
    password: str
    products: List[SimpleProduct] = []

    class Config:
        orm_mode = True


class SimpleUser(BaseModel):
    id: Optional[int] = None
    name: str
    phone: str

    class Config:
        orm_mode = True

class Product(BaseModel):
    id: Optional[int] = None
    name: str
    details: str
    price: float
    available: bool = False
    user_id: Optional[int]
    user: Optional[SimpleUser]

    class Config:
        orm_mode = True

class RequestsOrder(BaseModel):
    id: Optional[int] = None
    amount: int
    adress_delivery: Optional[str]
    type_delivery: str
    comments: Optional[str] = 'Sem observações'
    user_id: Optional[int]
    product_id: Optional[int]
    user: Optional[SimpleUser]
    products: Optional[SimpleProduct]
