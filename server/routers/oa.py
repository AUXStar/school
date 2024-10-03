from pony.orm import select, desc, db_session
from fastapi import APIRouter
from pydantic import BaseModel, conint, constr
from datetime import date,time

from utils.permission import permission_depends

from models.oa import OA
from models.user import User

api = APIRouter(prefix="/oa")


class OADetailLeave(BaseModel):
    date_from:date
    date_to:date
    time_from:time
    time_to:time
    reason:constr(max_length=200)  # type: ignore

class Summary(BaseModel):
    page_num: conint(ge=1) = 1  # type: ignore
    page_len: conint(le=40) = 10  # type: ignore


@api.get("/summary")
def summary(data:Summary,user:User=permission_depends("user")):
    with db_session:
        query = select(oa for oa in user.oa_to)
        query = query.sort_by(lambda oa: desc(oa.create_timestamp))
        query = select((oa.name, oa.create_timestamp,oa.type, oa.result,oa.from_user) for oa in query)
        query = query.page(data.page_num,data.page_len)
        return query.to_json()


class SubmitOA(BaseModel):
    name:constr(max_length=20)  # type: ignore
    detail:OADetailLeave


@api.get("/submit")
def submit(data:SubmitOA,user:User=permission_depends("oa.create")):
    with db_session:
        query = select(oa for oa in user.oa_to)
        query = query.sort_by(lambda oa: desc(oa.create_timestamp))
        query = select((oa.name, oa.create_timestamp,oa.type, oa.result,oa.from_user) for oa in query)
        query = query.page(data.page_num,data.page_len)
        return query.to_json()
