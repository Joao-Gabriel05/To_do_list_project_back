import dotenv
from pydantic import BaseModel
from typing import Literal, Optional, List
dotenv.load_dotenv()

class Project(BaseModel):
    _id: str
    tasks: List[str]
    members: List[str]
    status: Literal["não iniciado","em progresso","finalizado"]