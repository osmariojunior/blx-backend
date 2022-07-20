from requests import request
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    password =Column(String)
    phone = Column(String)

    products = relationship('Product', back_populates='user')
    request = relationship('Request', back_populates='user')

class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    details = Column(String)
    price = Column(Float)
    available = Column(Boolean)
    user_id = Column(Integer, ForeignKey('user.id', name='fk_user'))

    user = relationship('User', back_populates='products')


class Request(Base):
    __tablename__ = 'request'

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer)
    adress_delivery =Column(String)
    type_delivery = Column(String)
    comments = Column(String)
    user_id = Column(Integer, ForeignKey('user.id', name='fk_user_delivery'))
    product_id = Column(Integer, ForeignKey('product.id', name='fk_product_delivery'))

    products = relationship('Product')
    user = relationship('User', back_populates='request')