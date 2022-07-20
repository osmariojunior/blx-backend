from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import router_products, router_users


app = FastAPI()

# CORS

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# PRODUCTS

app.include_router(router_products.router)

# USERS

app.include_router(router_users.router)
