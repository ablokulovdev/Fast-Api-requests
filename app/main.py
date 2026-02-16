from fastapi import FastAPI
from app.db.database import initial_db
from app.routers.products import product_router


app = FastAPI(
    title="Shop"
)


initial_db()

app.include_router(product_router)


