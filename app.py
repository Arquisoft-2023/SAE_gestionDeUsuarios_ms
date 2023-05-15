from fastapi import FastAPI
from routes.bienestar import bienestar
from routes.estudiante import estudiante
from config.db import data_base_url,data_base_port,data_base_host

app =FastAPI()

app.include_router(bienestar)
app.include_router(estudiante)

print(data_base_url)
print(data_base_port)
print(data_base_host)