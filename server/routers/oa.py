#!/usr/bin/env python
# coding=utf-8
###
# @FilePath     : /school_backend/server/routers/oa.py
# @Author       : njzy njzy4688@gmail.com
# @Date         : 2024-09-23 13:37:26
# @LastEditors  : njzy njzy4688@gmail.com
# @LastEditTime : 2024-10-05 17:18:47
###
from pony.orm import select, desc, db_session
from fastapi import APIRouter
from pydantic import BaseModel, conint, constr
from datetime import date, time

from utils.permission import permission_depends

from models.oa import OA
from models.user import User

api = APIRouter(prefix="/oa")


class OADetailLeave(BaseModel):
    date_from: date
    date_to: date
    time_from: time
    time_to: time
    reason: constr(max_length=200)  # type: ignore


class SummaryFrom(BaseModel):
    page_num: conint(ge=1) = 1  # type: ignore
    page_len: conint(le=40) = 10  # type: ignore


@api.get("/summary_from")
def summary_from(data: SummaryFrom, user: User = permission_depends("user")):
    with db_session:
        query = select(oa for oa in user.oa_from)
        query = query.sort_by(lambda oa: desc(oa.create_timestamp))
        query = select(
            (oa.name, oa.create_timestamp, oa.type, oa.result, oa.from_user)
            for oa in query
        )
        query = query.page(data.page_num, data.page_len)
        return query.to_json()


class SummaryTo(BaseModel):
    page_num: conint(ge=1) = 1  # type: ignore
    page_len: conint(le=40) = 10  # type: ignore


@api.get("/summary_to")
def summary_to(data: SummaryTo, user: User = permission_depends("user")):
    with db_session:
        query = select(oa for oa in user.oa_to)
        query = query.sort_by(lambda oa: desc(oa.create_timestamp))
        query = select(
            (oa.name, oa.create_timestamp, oa.type, oa.result, oa.from_user)
            for oa in query
        )
        query = query.page(data.page_num, data.page_len)
        return query.to_json()


class SubmitOA(BaseModel):
    name: constr(max_length=20)  # type: ignore
    detail: OADetailLeave


@api.get("/submit")
def submit(data: SubmitOA, user: User = permission_depends("oa.create")):
    with db_session:
        oa = OA(
            name=data.name,
            details=data.detail.model_dump_json(),
            from_user=user,
            to_user=user.class_student.school_class.class_teacher.user,
        )
    return {"id":oa.id}
