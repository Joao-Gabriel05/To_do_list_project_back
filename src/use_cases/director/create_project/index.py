from repositories.project_repository import ProjectRepository
from .create_project_dto import CreateProjectDTO
from .create_project_use_case import CreateProjectUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()

create_project_use_case = CreateProjectUseCase(ProjectRepository())

@router.post("/director/create-project")
def create_project(create_project_dto:CreateProjectDTO, response:Response, request:Request):
    return create_project_use_case.execute(create_project_dto, response, request)

