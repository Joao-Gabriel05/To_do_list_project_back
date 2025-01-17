from repositories.project_repository import ProjectRepository
from use_cases.director.create_project.create_project_dto import CreateProjectDTO
from fastapi import Request, Response
from entities.project import Project

class GetProjectUseCase:
    def __init__(self, project_repository: ProjectRepository):
        self.project_repository = project_repository

    def execute(self, response: Response, request: Request):

        projects = self.project_repository.get_all_projects()
        if not projects:
            response.status_code = 407
            return {"status": "error"}
        
        response.status_code = 200
        return projects