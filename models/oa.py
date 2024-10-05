#!/usr/bin/env python
# coding=utf-8
###
# @FilePath     : /school_backend/models/oa.py
# @Author       : njzy njzy4688@gmail.com
# @Date         : 2024-09-22 12:21:36
# @LastEditors  : njzy njzy4688@gmail.com
# @LastEditTime : 2024-10-05 17:18:12
###
from pony.orm import Required, db_session, sum, Set, Optional, Json
from decimal import Decimal
from time import time
from enum import Enum
from .db import db


class OA(db.Entity):
    name = Required(str)
    create_timestamp = Required(int, default=lambda: int(time()))
    result_timestamp = Required(int, default=0)
    details = Required(Json)
    from_user = Set("User")
    to_user = Set("User")
    result = Required(int, default=0)

    # 0 pending 1 adopt -1 reject

    # result = Required(Json)
    # """
    # {
    #   "to":[
    #   {
    #     "result":
    #   },
    #   {}
    #   ]
    # }
    # """
