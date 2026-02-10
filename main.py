from fastapi import FastAPI
from routers import twosum

app = FastAPI()

app.include_router(twosum.router)