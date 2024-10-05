#!/usr/bin/env python
# coding=utf-8
###
# @FilePath     : /school_backend/server/routers/transaction.py
# @Author       : njzy njzy4688@gmail.com
# @Date         : 2024-09-10 23:53:12
# @LastEditors  : njzy njzy4688@gmail.com
# @LastEditTime : 2024-10-05 17:05:50
###
from models import TransactionDetail
from pony.orm import select, desc, db_session
from fastapi import APIRouter

api = APIRouter(prefix="/transaction")


@api.get("/summary")
def summary():
    with db_session:
        query = select(td for td in TransactionDetail)
        query = query.sort_by(lambda td: desc(td.timestamp))
        query = select((td.detail, td.money, td.timestamp) for td in query)
        query = query.page(1, 5)
        return query.to_json()
