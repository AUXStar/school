#!/usr/bin/env python
# coding=utf-8
###
# @FilePath     : /school_backend/models/transaction_detail.py
# @Author       : njzy njzy4688@gmail.com
# @Date         : 2024-09-14 22:19:14
# @LastEditors  : njzy njzy4688@gmail.com
# @LastEditTime : 2024-10-05 17:06:18
###
from pony.orm import Required, db_session, sum
from decimal import Decimal
from time import time

from .db import db


class TransactionDetail(db.Entity):
    class_ = Required("SchoolClass")
    detail = Required(str, 500)
    money = Required(Decimal, 10, 2)
    timestamp = Required(int, default=lambda: int(time()))

    @classmethod
    @db_session
    def total(cls):
        return sum(td.money for td in cls)
