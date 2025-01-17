from repositories.project_repository import ProjectRepository
from fastapi import Request, Response
from entities.project import Project
from use_cases.director.edit_project.edit_project_dto import EditProjectDTO

class EditProjectUseCase:
    def __init__(self, project_repository: ProjectRepository):
        self.project_repository = project_repository

    def execute(self, project_id: str, edit_project_dto: EditProjectDTO, response: Response, request: Request):
        self.project_repository.update(project_id, edit_project_dto)
            
        response.status_code = 200
        return {"status": "success", "message": "Projeto atualizado com sucesso"}
        # except ValueError as e:
        #     response.status_code = 404
        #     return {"status": "error", "message": str(e)}
        # except Exception as e:
        #     response.status_code = 500
        #     return {"status": "error", "message": "Erro ao atualizar o projeto"}
