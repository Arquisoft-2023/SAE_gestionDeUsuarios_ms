from fastapi import APIRouter
from  config.db import conn
from models.usuarios_roles_info import *

estudiante = APIRouter()

@estudiante.get("/estudiante/informacion_basica")
def get_users():
    return conn.execute(Usuarios.__table__.select()).fetchall()
