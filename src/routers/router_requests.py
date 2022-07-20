from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException
from src.infra.sqlalchemy.models.models import User
from src.infra.sqlalchemy.repositories.request import RepositoryRequest
from src.infra.sqlalchemy.config.database import get_db
from src.routers.auth_utils import get_user_logged
from src.schemas.schemas import RequestsOrder, SimpleRequestsOrder


router = APIRouter()


@router.post('/requests', status_code=status.HTTP_201_CREATED, response_model=SimpleRequestsOrder)
def create_request(request: RequestsOrder, session: Session = Depends(get_db)):
    try:
        request_created = RepositoryRequest(session).create(request)
        return request_created
    except:
        raise HTTPException(status_code=406)


@router.get('/requests', response_model=List[RequestsOrder])
def listem_request(session: Session = Depends(get_db)):
    try:
        request = RepositoryRequest(session).listem()
        return request
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'Not found Request')


@router.get('/requests/{id}', response_model=RequestsOrder)
def search_request(id: int , db: Session = Depends(get_db)):
    try: 
        request = RepositoryRequest(db).search(id)
        return request
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'Not found Request with ID = {id}')
    


@router.get('/request', response_model=List[RequestsOrder])
def sales(user: User = Depends(get_user_logged), db: Session = Depends(get_db)):
    request = RepositoryRequest(db).listem_sales_for_user_id(user.id)
    return request


@router.get('/requestspurchase', response_model=List[RequestsOrder])
def purchase(user: User = Depends(get_user_logged), db: Session = Depends(get_db)):
    request = RepositoryRequest(db).listem_purchase_for_user_id(user.id)
    return request



@router.put('/requests/{id}/', response_model=SimpleRequestsOrder)
def update_request(id: int, requests: RequestsOrder, db: Session = Depends(get_db)):
    RepositoryRequest(db).edit(id, requests)
    requests.id = id
    return requests
    

@router.delete('/requests/{id}')
def remove_request(id: int, db: Session = Depends(get_db)):
    try:
        RepositoryRequest(db).remove(id)
        return {'msg': 'Requests deleted.'}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'Not found Request with ID = {id}')
