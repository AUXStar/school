from models.db import db
from utils import instance_tools

def init_db():
    instance = instance_tools.CURRENT_INSTANCE
    db.bind(instance.config.db_connect)
    db.generate_mapping(create_tables=True)