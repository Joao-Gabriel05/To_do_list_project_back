from repositories.project_repository import ProjectRepository
from .get_project_use_case import GetProjectUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()

get_project_use_case = GetProjectUseCase(ProjectRepository())

@router.get("/director/get-project/{project_id}")
def get_project(project_id: str ,response:Response, request:Request):
    return get_project_use_case.execute(project_id,response, request)