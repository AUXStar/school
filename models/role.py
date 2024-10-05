#!/usr/bin/env python
# coding=utf-8
###
# @FilePath     : /school_backend/models/role.py
# @Author       : njzy njzy4688@gmail.com
# @Date         : 2024-09-19 13:10:25
# @LastEditors  : njzy njzy4688@gmail.com
# @LastEditTime : 2024-10-05 17:06:47
###
from pony.orm import Required, db_session, sum, Set, Optional
from decimal import Decimal
from time import time
from .db import db


class Teacher(db.Entity):
    user = Required("User")
    subject = Set("Subject")
    school_class = Set("SchoolClass")
    main_school_class = Optional("SchoolClass")


class Student(db.Entity):
    user = Required("User")
    school_class = Set("SchoolClass")
