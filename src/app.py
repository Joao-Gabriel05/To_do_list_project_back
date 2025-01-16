from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mongoengine import connect
import os
import glob
import dotenv
from importlib import import_module

connect(host=f"mongodb+srv://{os.getenv('MONGO_USER')}:{os.getenv('MONGO_PWD')}@aps5.ffbixcd.mongodb.net/")

dotenv.load_dotenv()


app = FastAPI()

@app.get("/")
def test():
    return {"status": "OK v2 (3)"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://0.0.0.0:8000"],    #coloque aqui a URL do front-end permitido
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

working_directory = os.path.dirname(os.path.abspath(__file__))
use_cases_directory = os.path.join(working_directory, "use_cases")
routes = glob.glob(os.path.join(use_cases_directory, "**/index.py"), recursive=True)

for route in routes:
    relative_path = os.path.relpath(route, working_directory)
    module_name = os.path.splitext(relative_path)[0].replace(os.path.sep, '.')

    try:
        module = import_module(module_name)
        if hasattr(module, 'router'):
            app.include_router(module.router)
    except ModuleNotFoundError as e:
        print(f"Erro ao importar módulo {module_name}: {e}")