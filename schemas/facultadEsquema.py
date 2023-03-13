from pydantic  import BaseModel
#from typing import Optional

class FacultadEsquema(BaseModel):

    id_facultad : int
    nombre_facultad : str

    class Config:
        orm_mode = True

class FacultadDepartamentoEsquema(BaseModel):

    id_facultad : int
    id_departamento : str

    class Config:
        orm_mode = True