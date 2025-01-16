from pydantic import BaseModel
from typing import Literal, Optional

class CreateProjectDTO(BaseModel):
    tasks: list[str]
    members: list[str]
    status: Literal["não iniciado","em progresso","finalizado"]