from models.transaction_detail import db
from pony.orm import db_session,select
from utils import instance_tools,permission,database

ins = instance_tools.Instance('instance1')


database.init_db()

permission.init_permission()