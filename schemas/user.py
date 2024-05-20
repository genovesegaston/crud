from typing import Optional
from pydantic import BaseModel
from pydantic.config import ConfigDict



class User(BaseModel):
  
  id: Optional[int] = None
  name:str
  password:str
  email:str

class UserResponse(BaseModel):
  
  id: str | None = None
  name:str
  password:str
  email:str
