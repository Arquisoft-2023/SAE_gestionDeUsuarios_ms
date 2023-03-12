from pydantic  import BaseModel
#from typing import Optional

class DepartamentoEsquema(BaseModel):

    id_departamento : int
    nombre_departamento : str

    class Config:
        orm_mode = True

class DepartamentoProgramasEsquema(BaseModel):

    codigo_programa : int    
    id_departamento : int
    

    class Config:
        orm_mode = True
