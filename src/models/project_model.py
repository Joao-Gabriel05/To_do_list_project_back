from mongoengine import *
import datetime
from models.fields.sensivity_field import SensivityField
import os
import dotenv
import bcrypt
from cryptography.fernet import Fernet

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class ProjectModel(Document):
    sensivity_fields = [
        
    ]

    tasks = ListField(StringField(), required = True)
    members = ListField(StringField(), required = True)
    status = StringField(required=True)

    



    def get_normal_fields():
        return [i for i in ProjectModel.__dict__.keys() if i[:1] != '_' and i != "sensivity_fields" and i not in ProjectModel.sensivity_fields]
    
