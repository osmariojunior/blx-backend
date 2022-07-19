from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    id: Optional[str] = None
    name: str
    tel: str

class Product(BaseModel):
    id: Optional[str] = None
    name: str
    details: str
    price: float
    available: bool = False

    class Config:
        orm_mode = True

class RequestsOrder(BaseModel):
    id: Optional[str] = None
    user: User
    product: Product
    amount: int
    delivery: bool = True
    address: str
    comments: Optional[str] = 'Sem observações'