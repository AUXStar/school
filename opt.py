from database.models import TransactionDetail,connect_db
from pony.orm import db_session,select

connect_db()

with db_session:
    select((td.detail,td.money) for td in TransactionDetail).show()
    