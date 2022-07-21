# 
FROM python:3.9

# 
WORKDIR /code

#
RUN python -m pip install --upgrade pip

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./src /code/app

#
EXPOSE 8000
CMD ["uvicorn", "src.server:app", "--host", "127.0.0.1", "--port", "8000"]
