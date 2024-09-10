from fastapi import FastAPI
from database import models
from instance import config
models.connect_db(models.db,config.db_connect)

def create_app():
    app = FastAPI(title='school_backend')
    from .routers import include_routers
    include_routers(app)
    return app