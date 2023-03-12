from pydantic  import BaseModel
#from typing import Optional

class UsuarioEsquema(BaseModel):
    usuario_un : str
    estado : bool
    nombres : str
    apellidos : str
    documento : str
    tipo_documento : bool

    class Config:
        orm_mode = True
