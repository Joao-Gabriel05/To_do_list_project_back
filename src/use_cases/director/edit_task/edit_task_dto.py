from pydantic import BaseModel
from typing import Literal, Optional

class EditTaskDTO(BaseModel):
    _id: str
    status: Literal["não iniciado","em progresso","finalizado"]
    members: list[str]
    priority : Literal["pouco importante","importante","muito importante"]
    title:str
    due_date: str
