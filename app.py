from fastapi import FastAPI
from routes.usuarios import usuarios

app =FastAPI()

app.include_router(usuarios)
