from pydantic  import BaseModel
#from typing import Optional

class FacultadEsquema(BaseModel):

    id_facultad : int
    nombre_facultad : str

    class Config:
        orm_mode = True
