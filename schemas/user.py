from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
  id: Optional[str] = None
  name:str
  password:str
  email:str

gaston = User(name="gaston",password="asd",email="asdasd")
print(gaston)