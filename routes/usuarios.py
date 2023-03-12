from fastapi import APIRouter
from  config.db import conn
from models.usuarios_roles_info import *

usuarios = APIRouter()

@usuarios.get("/usuarios")
def get_users():
    return conn.execute(Usuarios.select()).fetchall()

@usuarios.get("/usuarios")
def hello():
    return "hello2"

@usuarios.get("/usuarios")
def hello():
    return "hello2"

@usuarios.get("/usuarios")
def hello():
    return "hello2"

@usuarios.get("/usuarios")
def hello():
    return "hello2"