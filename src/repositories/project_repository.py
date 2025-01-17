import os
import bcrypt
import dotenv
from typing import List
from mongoengine import *
from cryptography.fernet import Fernet
from entities.project import Project
from models.project_model import ProjectModel
from models.fields.sensivity_field import SensivityField
from utils.encode_hmac_hash import encode_hmac_hash

class ProjectRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, project: Project) -> None:
        project_model = ProjectModel()
        project_dict = project.model_dump()

        for k in ProjectModel.get_normal_fields():
            if (k not in project_dict):
                continue

            project_model[k] = project_dict[k]

        for k in ProjectModel.sensivity_fields:
            project_model[k] = SensivityField(fernet=self.fernet, data=project_dict[k])

    

        project_model.save()

        return None
    
    def get_project_by_id(self, project_id: str) -> dict:
        project = ProjectModel.objects.with_id(project_id)
        if not project:
            return None
        project_dict = project.to_mongo().to_dict()
        project_dict['_id'] = str(project_dict['_id'])
        return project_dict
    
    def update(self,project_id:str,updated_data:dict)->None:
        project = ProjectModel.objects.with_id(project_id)
        updated_data = updated_data.model_dump()
        if not project:
            raise ValueError("Projeto não encontrado")
        for key, value in updated_data.items():
            if hasattr(project, key):
                setattr(project, key, value)

        project.save()

    def get_all_projects(self) -> List[dict]:

        projects = ProjectModel.objects()
        result = []

        for project in projects:
            project_dict = project.to_mongo().to_dict()
            project_dict['_id'] = str(project_dict['_id']) 
            result.append(project_dict)

        return result

    def delete_project(self,project_id:str)->dict:
        project = ProjectModel.objects.with_id(project_id)
        if not project:
            return False
        project.delete()
        return True