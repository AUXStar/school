from models.transaction_detail import db,TransactionDetail,connect_db
from pony.orm import db_session,select
from utils import instance_tools

ins = instance_tools.Instance()


connect_db(db,ins.instance_import('config').db_connect)

with db_session:
    select((td.detail,td.money) for td in TransactionDetail).show()