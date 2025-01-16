from repositories.project_repository import ProjectRepository
from .edit_project_dto import EditProjectDTO
from .edit_project_use_case import EditProjectUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()

edit_project_use_case = EditProjectUseCase(ProjectRepository())
@router.put("/director/edit-project/{project_id}")
def edit_project(project_id: str, edit_project_dto: EditProjectDTO, response: Response, request: Request):
    return edit_project_use_case.execute(project_id, edit_project_dto, response, request)