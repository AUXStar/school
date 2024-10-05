#!/usr/bin/env python
# coding=utf-8
###
# @FilePath     : /school_backend/models/school_class.py
# @Author       : njzy njzy4688@gmail.com
# @Date         : 2024-09-19 13:12:40
# @LastEditors  : njzy njzy4688@gmail.com
# @LastEditTime : 2024-10-05 17:06:40
###
from pony.orm import Required, db_session, sum, Set, Optional
from decimal import Decimal
from time import time
from .db import db


class SchoolClass(db.Entity):
    name = Required(str)
    grade = Required(int)
    number = Required(int)
    students = Set("Student")
    teachers = Set("Teacher")
    class_teacher = Required("Teacher", reverse="main_school_class")
    transactions = Set("TransactionDetail")
    time_slot_table = Optional("TimeSlotTable")
