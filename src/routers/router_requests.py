from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException
from src.infra.sqlalchemy.config.database import get_db
from src.schemas.schemas import RequestsOrder


router = APIRouter()


@router.post('/requests', status_code=status.HTTP_201_CREATED, response_model=RequestsOrder)
def create_request(request: RequestsOrder, session: Session = Depends(get_db)):
    pass

@router.get('/requests', response_model=List[RequestsOrder])
def listem_request(sessino: Session = Depends(get_db)):
    pass


@router.get('/requests/{id}')
def search_request(id: int , db: Session = Depends(get_db)):
    pass
