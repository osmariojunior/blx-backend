from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import router_products, router_users, router_requests

# DOCS

tags_metadata = [
    {
        "name": "Users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "Products",
        "description": "Route of Products",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://github.com/osmariojunior",
        },
    },
    {
        "name": "Requests Order",
        "description": "Route of Requests Order.",
    },
]



app = FastAPI(openapi_tags=tags_metadata)

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

app.include_router(router_products.router, tags=['Products'])

# USERS

app.include_router(router_users.router, tags=['Users'])


# REQUESTS ORDER

app.include_router(router_requests.router, tags=['Requests Order'])
