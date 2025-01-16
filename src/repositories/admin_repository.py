import os
import bcrypt
import dotenv
from typing import List
from mongoengine import *
from cryptography.fernet import Fernet
from entities.admin import Admin
from models.admin_model import AdminsModel
from models.fields.sensivity_field import SensivityField
from utils.encode_hmac_hash import encode_hmac_hash

class AdminRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, admin: Admin) -> None:
        admin_model = AdminsModel()
        admin_dict = admin.model_dump()

        for k in AdminsModel.get_normal_fields():
            if (k not in admin_dict):
                continue

            admin_model[k] = admin_dict[k]

        for k in AdminsModel.sensivity_fields:
            admin_model[k] = SensivityField(fernet=self.fernet, data=admin_dict[k])

        admin_model.password = bcrypt.hashpw(f'{admin.password}'.encode(), bcrypt.gensalt()).decode()

        admin_model.save()

        return None
    
    def find_by_email(self, email: str) -> list[AdminsModel]:
        result = AdminsModel.objects(email=email)
        return result
    
    def find_by_id(self, id: str) -> list[AdminsModel]:
        result = AdminsModel.objects(id=id)
        return result
    
    def update_reset_pwd_token(self, email: str, sent_at: int, token: str) -> None:
        AdminsModel.objects(email=email).update(set__reset_pwd_token_sent_at=sent_at, set__reset_pwd_token=token)

        return None
    
    def find_by_reset_pwd_token(self, token) -> list[AdminsModel]:
        result: list[AdminsModel] = AdminsModel.objects(reset_pwd_token=token)

        return result
    
    def update_pwd(self, id: str, pwd: str) -> None:
        AdminsModel.objects(id=id).update(set__password = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode())

        return None
    
    def get_name(self, id: str) -> str:
        director = AdminsModel.objects(id=id).first()
        if director:
            return director.name

    def get_email(self, id: str) -> str:
        director = AdminsModel.objects(id=id).first()
        if director:
            return director.email
    
    def update_name(self, id: str, name: str) -> None:
        AdminsModel.objects(id=id).update(set__name = name)
        return None

    def update_email(self, id: str, email: str) -> None:
        AdminsModel.objects(id=id).update(set__email = email)
        return None