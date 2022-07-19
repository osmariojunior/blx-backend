from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    id: Optional[str] = None
    name: str
    tel: str
    my_products: List[Product]
    my_sales: List[Product]
    my_requests: List[RequestsOrder]

class Product(BaseModel):
    id: Optional[str] = None
    name: str
    details: str
    price: float
    available: bool = False

class RequestsOrder(BaseModel):
    id: Optional[str] = None
    user: User
    product: Product
    amount: int
    delivery: bool = True
    address: str
    comments: Optional[str] = 'Sem observações'