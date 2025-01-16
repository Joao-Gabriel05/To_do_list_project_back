from repositories.project_repository import ProjectRepository
from use_cases.director.create_project.create_project_dto import CreateProjectDTO
from fastapi import Request, Response
from entities.project import Project

class CreateProjectUseCase:
    def __init__(self, project_repository: ProjectRepository):
        self.project_repository = project_repository

    def execute(self, create_project_dto: CreateProjectDTO, response: Response, request: Request):
        if not create_project_dto.tasks or not create_project_dto.members or not create_project_dto.status:
            response.status_code = 407
            return {"status": "error", "message":"faltam informações"}

        project = Project(
            tasks=create_project_dto.tasks,
            members=create_project_dto.members,
            status=create_project_dto.status,
        )

        self.project_repository.save(project)
        response.status_code=201
        return {"status": "success", "message":"Projeto criado"}
