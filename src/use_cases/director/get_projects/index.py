from repositories.project_repository import ProjectRepository
from .get_project_use_case_by_id import GetProjectByIDUseCase
from fastapi import Request, Response, APIRouter
from .get_project_use_case import GetProjectUseCase

router = APIRouter()

get_project_by_id_use_case = GetProjectByIDUseCase(ProjectRepository())
get_project_use_case= GetProjectUseCase(ProjectRepository())


@router.get("/director/get-project/{project_id}")
def get_project_by_id(project_id: str ,response:Response, request:Request):
    return get_project_by_id_use_case.execute(project_id,response, request)

@router.get("/director/get-project")
def get_project(response:Response, request:Request):
    return get_project_use_case.execute(response, request)
