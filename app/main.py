from fastapi import FastAPI
from app.db.database import initial_db


app = FastAPI()

initial_db()


