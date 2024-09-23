from pony.orm import select, desc, db_session
from fastapi import APIRouter
from pydantic import BaseModel, conint

from utils.permission import permission_depends

from models.oa import OA
from models.user import User

api = APIRouter(prefix="/oa")


class Summary(BaseModel):
    page_num: conint(ge=1) = 1  # type: ignore
    page_len: conint(le=40) = 10  # type: ignore


@api.get("/summary")
def summary(user=permission_depends("user")):
    with db_session:
        query = select(td for td in OA)
        query = query.sort_by(lambda td: desc(td.timestamp))
        query = select((td.detail, td.money, td.timestamp) for td in query)
        query = query.page(1, 5)
        return query.to_json()
