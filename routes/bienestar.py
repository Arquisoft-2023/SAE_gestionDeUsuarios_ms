from fastapi import APIRouter

#Conexion a la base de datos
from  config.db import conn
from  config.db import session

#Modelos
from models.usuarios_roles_info import *
from models.programas_facultades_departamentos import *


#Esquemas
from schemas.rolEsquema import *
from schemas.usuarioEsquema import *
from schemas.departamentoEsquema import *
from schemas.facultadEsquema import *
from schemas.programaEsquema import *

#Lectura de archivos no dict
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

@bienestar.delete("/bienestar/usuarios/rol/usuariosRol/{usuario_un}")
def eliminar_usuario_y_rol(usuario_un_elim: str):
        
    usuario_y_rol_a_eliminar = conn.execute(t_usuario_rol.delete().where(t_usuario_rol.c.usuario_un == usuario_un_elim))
    conn.commit()
        
    return "Usuario y rol eliminado"

@bienestar.put("/bienestar/usuarios/rol/usuariosRol/{usuario_un}&{rol_id}")
def modificar_usuario_y_rol(usuario_un_a_buscar: str, rol_id_nuevo: int):

    conn.execute(t_usuario_rol.update().values(rol_id=rol_id_nuevo).where(t_usuario_rol.c.usuario_un == usuario_un_a_buscar))
    conn.commit()
    return "usuario y rol modificado"

#Departamentos

@bienestar.get("/bienestar/informacionUniversidad/departamentos", response_model= list[DepartamentoEsquema])
def leer_departametos():
    result = session.query(Departamentos).all()
    return result

@bienestar.post("/bienestar/informacionUniversidad/departamentos", response_model= list[DepartamentoEsquema])
def agregar_departameto(departamento_nuevo: str):
    conn.execute(Departamentos.__table__.insert().values({"nombre_departamento":departamento_nuevo}))
    conn.commit()
    return session.query(Departamentos).all()

@bienestar.put("/bienestar/informacionUniversidad/departamentos/{departamento_id}", response_model= DepartamentoEsquema)
def modificar_nombre_departamento(departamento_a_econtrar: int,datos_nuevo_departamento: str):
        
    departamento_a_modificar = session.query(Departamentos).get(departamento_a_econtrar)
    departamento_a_modificar.nombre_departamento =datos_nuevo_departamento
    session.commit()
        
    return session.query(Departamentos).get(departamento_a_econtrar)

@bienestar.delete("/bienestar/informacionUniversidad/departamentos/{departamento_id}")
def eliminar_departamento(departamento_a_econtrar: int):
            
    departamento_a_eliminar = session.query(Departamentos).get(departamento_a_econtrar)
    session.delete(departamento_a_eliminar)
    session.commit()
            
    return session.query(Departamentos).all()

#Facultades

@bienestar.get("/bienestar/informacionUniversidad/facultades", response_model= list[FacultadEsquema])
def leer_facultades():
    result = session.query(Facultad).all()
    return result

@bienestar.post("/bienestar/informacionUniversidad/facultades", response_model= list[FacultadEsquema])
def agregar_facultad(facultad_nueva: str):
    session.add(Facultad(nombre_facultad=facultad_nueva))
    session.commit()
    return session.query(Facultad).all()

@bienestar.put("/bienestar/informacionUniversidad/facultades/{facultad_id}", response_model= FacultadEsquema)
def modificar_nombre_facultad(facultad_nombre_nuevo: str,facultad_a_modificar: int):
        
    facultad_a_modificar_dato = session.query(Facultad).get(facultad_a_modificar)
    facultad_a_modificar_dato.nombre_facultad =facultad_nombre_nuevo
    session.commit()
        
    return session.query(Facultad).get(facultad_a_modificar)

@bienestar.delete("/bienestar/informacionUniversidad/facultades/{facultad_id}")
def eliminar_facultad(facultad_a_econtrar: int):
                
    facultad_a_eliminar = session.query(Facultad).get(facultad_a_econtrar)
    session.delete(facultad_a_eliminar)
    session.commit()
                
    return session.query(Facultad).all()

#Programas facultad
@bienestar.get("/bienestar/informacionUniversidad/programasAcademicos", response_model= list[ProgramaEsquema])
def leer_programas_academicos():
    result = session.query(ProgramasAcademicos).all()
    return result

@bienestar.post("/bienestar/informacionUniversidad/programasAcademicos")
def agregar_programa_academico(programa_nuevo: str, codigo_programa_nuevo: int):
    session.add(ProgramasAcademicos(nombre_programa=programa_nuevo,codigo_programa=codigo_programa_nuevo))
    session.commit()
    return session.query(ProgramasAcademicos).get(codigo_programa_nuevo)

@bienestar.put("/bienestar/informacionUniversidad/programasAcademicos/{programa_id}", response_model= ProgramaEsquema)
def modificar_nombre_programa(programa_nombre_nuevo: str,programa_a_modificar: int):
            
    programa_a_modificar_dato = session.query(ProgramasAcademicos).get(programa_a_modificar)
    programa_a_modificar_dato.nombre_programa =programa_nombre_nuevo
    session.commit()
    result = session.query(ProgramasAcademicos).get(programa_a_modificar)
            
    return result

@bienestar.delete("/bienestar/informacionUniversidad/programasAcademicos/{programa_id}")
def eliminar_programa(programa_a_econtrar: int):
                        
    programa_a_eliminar = session.query(ProgramasAcademicos).get(programa_a_econtrar)
    session.delete(programa_a_eliminar)
    session.commit()
                        
    return session.query(ProgramasAcademicos).all()

#DepartamentoProgramas

@bienestar.get("/bienestar/informacionUniversidad/departamentoProgramas", response_model= list[DepartamentoProgramasEsquema])
def leer_departamento_programas():
    result = session.query(t_departamento_programas).all()
    return result

@bienestar.post("/bienestar/informacionUniversidad/departamentoProgramas")
def agregar_departamento_programa(codigo_programa_nu: int, id_departamento_nu: int):
    session.add(t_departamento_programas(codigo_programa=codigo_programa_nu,id_departamento=id_departamento_nu))
    session.commit()
    return session.query(t_departamento_programas).get(codigo_programa_nu,id_departamento_nu)