from fastapi import FastAPI
from routes.bienestar import bienestar
from routes.estudiante import estudiante

app =FastAPI()

app.include_router(bienestar)
app.include_router(estudiante)