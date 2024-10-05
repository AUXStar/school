#!/usr/bin/env python
# coding=utf-8
###
# @FilePath     : /school_backend/models/notice.py
# @Author       : njzy njzy4688@gmail.com
# @Date         : 2024-09-23 12:51:46
# @LastEditors  : njzy njzy4688@gmail.com
# @LastEditTime : 2024-10-05 17:07:20
###
from pony.orm import Required, db_session, sum, Set, Optional, Json
from decimal import Decimal
from time import time
from .db import db


class Notice(db.Entity):
    title = Required(str)
    details = Required(Json)
    from_user = Set("User")
    to_user = Set("User")
    type = Required(int)
    result = Required(int)
    create_timestamp = Required(int, default=lambda: int(time()))
    result_timestamp = Required(int, default=0)
