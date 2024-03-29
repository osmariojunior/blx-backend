from sys import prefix
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from src.routers import router_auth, router_products, router_requests

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

app.include_router(router_auth.router, prefix="/auth", tags=['Users'])

# REQUESTS ORDER

app.include_router(router_requests.router, tags=['Requests Order'])

# MIDDLEWARES

@app.middleware('http')
async def process_time_required(req: Request, next):
    print('Interceptor arrive...')
    res = await next(req)
    print('Interceptor back...')
    return res