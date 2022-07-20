from datetime import datetime, timedelta
from jose import jwt


#CONFIG

SECRET_KEY = 'caa9c8f8620cbb30679026bb6427e11f'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 3000


def create_access_token(data: dict):
    datas = data.copy()
    expiration = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)

    datas.update({'exp': expiration})

    token_jwt = jwt.encode(datas, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt


def verify_access_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload.get('sub')

