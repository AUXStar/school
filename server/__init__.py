from fastapi import FastAPI
from utils import instance_tools
import sys
import os

def create_app(instance_dir=None,base_dir=None):
    sys.path.append(os.path.abspath(os.path.join(os.path.split(os.path.abspath(__file__))[0],"..")))
    print(sys.path)
    instance_tools.init_instance(instance_dir,base_dir)
    app = FastAPI(title='school_backend')
    from .routers import include_routers
    include_routers(app)
    return app