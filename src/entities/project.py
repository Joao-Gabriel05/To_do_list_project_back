import dotenv
from pydantic import BaseModel
from typing import Literal,List
dotenv.load_dotenv()

class Project(BaseModel):
    _id: str
    name: str
    tasks: List[str]
    memebers: List[str]
    

