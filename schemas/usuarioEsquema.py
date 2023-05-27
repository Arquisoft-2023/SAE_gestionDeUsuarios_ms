from pydantic  import BaseModel
import datetime
#from typing import Optional

class UsuarioEsquema(BaseModel):
    usuario_un : str
    estado : bool
    nombres : str
    apellidos : str
    documento : str
    tipo_documento : bool
    token_web : str
    token_movile : str

    class Config:
        orm_mode = True

class UsuarioRolEsquema(BaseModel):
    rol_id : int
    usuario_un : str

    class Config:
        orm_mode = True

class InformacionPersonalEsquema(BaseModel):

    fecha_nacimiento : datetime.date 
    sexo : bool
    ciudad_nacimiento : str
    direccion_residencia : str
    ciudad_residencia : str
    telefono : str
    correo_alterno : str
    eps : str
    hijos : bool
    nombre_apellido_acudiente : str
    relacion_acudiente : str
    telefono_acudiente : str
    usuario_un : str

    class Config:
        orm_mode = True

class InformacionAcademicaEsquema(BaseModel):

    historia_academica : int
    porcentaje_de_avance : float
    estado_historia : bool
    papi : float
    papa : float
    codigo_programa_academico : int

    class Config:
        orm_mode = True

class InformacionAcademicaEstudianteEsquema(BaseModel):

    cod_historia_academica : int
    usuario_un : str

    class Config:
        orm_mode = True