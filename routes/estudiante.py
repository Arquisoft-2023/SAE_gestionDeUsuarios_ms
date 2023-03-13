from fastapi import APIRouter

#Conexion a la base de datos
from  config.db import conn
from  config.db import session


from models.usuarios_roles_info import InformacionPersonal
from schemas.usuarioEsquema import InformacionPersonalEsquema

estudiante = APIRouter()

#InformacionPersonal

@estudiante.get("/estudiante/informacionPersonal/{usuario_un}", response_model= InformacionPersonalEsquema)
def leer_informacion_personal_del_estudiante(usuario_un : str):
    result = session.query(InformacionPersonal).get(usuario_un)
    return result

@estudiante.post("/estudiante/informacionPersonal", response_model= InformacionPersonalEsquema)
def ingresar_informacion_personal_del_estudiante(nueva_informacion: InformacionPersonalEsquema):

    conn.execute(InformacionPersonal.__table__.insert().values(nueva_informacion.dict()))
    conn.commit()

    return session.query(InformacionPersonal).get(nueva_informacion.usuario_un)
    
@estudiante.put("/estudiante/informacionPersonal/{usuario_un}", response_model= InformacionPersonalEsquema)
def modificar_informacion_personal_del_estudiante(nueva_informacion: InformacionPersonalEsquema):
    
    session.query(InformacionPersonal).filter(InformacionPersonal.usuario_un == nueva_informacion.usuario_un).update(nueva_informacion.dict())
    session.commit()
    
    return session.query(InformacionPersonal).get(nueva_informacion.usuario_un)

@estudiante.delete("/estudiante/informacionPersonal/{usuario_un}")
def eliminar_informacion_personal_del_estudiante(usuario_un: str):
    session.query(InformacionPersonal).filter(InformacionPersonal.usuario_un == usuario_un).delete()
    session.commit()
    return {"mensaje": "Informacion personal del estudiante eliminada"}