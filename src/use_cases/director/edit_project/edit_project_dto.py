from pydantic import BaseModel
from typing import List, Optional

class EditProjectDTO(BaseModel):
    tasks: Optional[List[str]] = None
    members: Optional[List[str]] = None
    status: Optional[str] = None
