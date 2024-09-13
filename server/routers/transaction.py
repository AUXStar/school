from models.transaction_detail import TransactionDetail
from pony.orm import select, desc, db_session
from fastapi import APIRouter

api = APIRouter(prefix='/transaction')

@api.get('/summary')
def summary():
    with db_session:
        query = select(td for td in TransactionDetail)
        query = query.sort_by(lambda td:desc(td.timestamp))
        query = select((td.detail,td.money,td.timestamp) for td in query)
        query = query.page(1,5)
        return query.to_json()
