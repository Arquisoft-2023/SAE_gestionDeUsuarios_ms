from pydantic  import BaseModel
#from typing import Optional

class RolEsquema(BaseModel):
    rol : str
    rol_id :int

    class Config:
        orm_mode = True
