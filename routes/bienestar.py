from fastapi import APIRouter
from  config.db import conn
from  config.db import session
from models.usuarios_roles_info import *
from schemas.rolEsquema import *
from schemas.usuarioEsquema import *
import ast

bienestar = APIRouter()

#Usuarios

@bienestar.get("/bienestar/usuarios", response_model= list[UsuarioEsquema])
def leer_usuarios():
    result = session.query(Usuarios).all()
    return result

@bienestar.get("/bienestar/usuarios/{usuario_un}", response_model= UsuarioEsquema)
def buscar_un_usuario(usuario_un_a_buscar: str):
    return session.query(Usuarios).get(usuario_un_a_buscar)

@bienestar.post("/bienestar/usuarios", response_model= UsuarioEsquema)
def ingresar_usuario(nuevo: UsuarioEsquema):

    #Forma de hacerlo con SQLAlchemy Session - mas largo pero formal

    #datos_nuevo_usuario = Usuarios(
    #    usuario_un = nuevo.usuario_un,
    #    estado = nuevo.estado,
    #    nombres = nuevo.nombres,
    #    apellidos = nuevo.apellidos,
    #    documento = nuevo.documento,
    #    tipo_documento = nuevo.tipo_documento
    #)

    #session.commit()
    
    #result = session.query(Usuarios).all()
    #return result

    conn.execute(Usuarios.__table__.insert().values(nuevo.dict()))
    conn.commit()

    return session.query(Usuarios).get(nuevo.usuario_un)

@bienestar.put("/bienestar/usuarios/{usuario_un}&{estado}", response_model= UsuarioEsquema)
def modificar_estado_usuario(usuario_un_a_buscar: str, estado_nuevo: bool):
    
    usuario_a_modificar = session.query(Usuarios).get(usuario_un_a_buscar)
    usuario_a_modificar.estado = estado_nuevo
    session.commit()
    return session.query(Usuarios).get(usuario_un_a_buscar)

@bienestar.put("/bienestar/usuarios/{usuario_un}", response_model= UsuarioEsquema)
def modificar_datos_usuario(usuario_un_a_econtrar: str,datos_nuevos_usuario: UsuarioEsquema):
    
    usuario_a_modificar = session.query(Usuarios).get(usuario_un_a_econtrar)
    usuario_a_modificar.usuario_un =datos_nuevos_usuario.dict().get("usuario_un")
    usuario_a_modificar.estado =datos_nuevos_usuario.dict().get("estado")
    usuario_a_modificar.nombres =datos_nuevos_usuario.dict().get("nombres")
    usuario_a_modificar.apellidos =datos_nuevos_usuario.dict().get("apellidos")
    usuario_a_modificar.documento =datos_nuevos_usuario.dict().get("documento")
    usuario_a_modificar.tipo_documento =datos_nuevos_usuario.dict().get("tipo_documento")
    session.commit()
    
    return session.query(Usuarios).get(usuario_a_modificar.usuario_un)



#Roles

@bienestar.get("/bienestar/usuarios/rol", response_model= list[RolEsquema])
def leer_roles():
    result = session.query(Rol).all()
    return result

@bienestar.post("/bienestar/usuarios/rol", response_model= list[RolEsquema])
def ingresar_rol(nuevo_rol: str):

    conn.execute(Rol.__table__.insert().values({"rol":nuevo_rol}))
    conn.commit()
    return session.query(Rol).all()

@bienestar.put("/bienestar/usuarios/rol/{rol_id}", response_model= RolEsquema)
def modificar_nombre_rol(rol_a_econtrar: int,datos_nuevo_rol: str):
    
    rol_a_modificar = session.query(Rol).get(rol_a_econtrar)
    rol_a_modificar.rol =datos_nuevo_rol
    session.commit()
    
    return session.query(Rol).get(rol_a_econtrar)

@bienestar.delete("/bienestar/usuarios/rol/{rol_id}")
def eliminar_rol(rol_a_econtrar: int):
        
    rol_a_eliminar = session.query(Rol).get(rol_a_econtrar)
    session.delete(rol_a_eliminar)
    session.commit()
        
    return session.query(Rol).all()

#Usuarios Roles
@bienestar.post("/bienestar/usuarios/rol/{usuario_un}&{rol_id}")
def ingresar_usuario_rol(usuario_un_a_buscar: str, rol_id_a_buscar: int):
    
    conn.execute(t_usuario_rol.insert().values(usuario_un=usuario_un_a_buscar,rol_id=rol_id_a_buscar))
    conn.commit()
    return ast.literal_eval(str(conn.execute(t_usuario_rol.select()).fetchall()))

@bienestar.get("/bienestar/usuarios/rol/usuariosRol")
def leer_roles_de_usuarios():
    return ast.literal_eval(str(conn.execute(t_usuario_rol.select()).fetchall()))