from repositories.project_repository import ProjectRepository
from .delete_project_use_case import DeleteProjectUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()

create_project_use_case = DeleteProjectUseCase(ProjectRepository())

@router.delete("/director/create-project/{project_id}")
def delete_project(project_id:str,response:Response, request:Request):
    return create_project_use_case.execute(project_id, response, request)

