from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
  id:Optional[str]
  name:str
  password:str
  email:str