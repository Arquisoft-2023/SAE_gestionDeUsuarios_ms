from pydantic  import BaseModel
#from typing import Optional

class ProgramaEsquema(BaseModel):

    codigo_programa : int
    nombre_programa : str

    class Config:
        orm_mode = True
