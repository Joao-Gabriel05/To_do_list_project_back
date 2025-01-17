from repositories.project_repository import ProjectRepository
from fastapi import Request, Response
from entities.project import Project

class DeleteProjectUseCase:
    def __init__(self, project_repository: ProjectRepository):
        self.project_repository = project_repository

    def execute(self, project_id: str, response: Response, request: Request):

        project = self.project_repository.get_project_by_id(project_id)
        if not project:
            response.status_code = 407
            return {"status": "error"}
        
        response.status_code = 200
        return project
