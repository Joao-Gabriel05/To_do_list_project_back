import dotenv
from pydantic import BaseModel
from typing import Literal, Optional, List
dotenv.load_dotenv()

class Task(BaseModel):
    _id: str
    status: Literal["não iniciado","em progresso","finalizado"]
    members: List[str]
    priority : Literal["pouco importante","importante","muito importante"]
    title:str
    duo_date: str
