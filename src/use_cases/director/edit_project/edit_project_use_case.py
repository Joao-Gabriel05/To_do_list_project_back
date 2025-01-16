from repositories.project_repository import ProjectRepository
from use_cases.director.create_project.create_project_dto import CreateProjectDTO
from fastapi import Request, Response
from entities.project import Project

class EditProjectUseCase:
    def __init__(self, project_repository: ProjectRepository):
        self.project_repository = project_repository

    def execute(self, project_id: str, update_project_dto: CreateProjectDTO, response: Response, request: Request):
        # Verificar se o projeto existe
        existing_project = self.project_repository.get_project_by_id(project_id)
        if not existing_project:
            response.status_code = 404
            return {"status": "error", "message": "Projeto não encontrado"}

        # Validar informações de entrada
        if not update_project_dto.tasks or not update_project_dto.members or not update_project_dto.status:
            response.status_code = 400
            return {"status": "error", "message": "Faltam informações para atualizar o projeto"}

        # Atualizar os dados do projeto
        existing_project.tasks = update_project_dto.tasks
        existing_project.members = update_project_dto.members
        existing_project.status = update_project_dto.status

        # Salvar as alterações no repositório
        self.project_repository.save(existing_project)

        response.status_code = 200
        return {"status": "success", "message": "Projeto atualizado com sucesso"}