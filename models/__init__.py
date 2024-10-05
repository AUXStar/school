#!/usr/bin/env python
# coding=utf-8
###
# @FilePath     : /school_backend/models/__init__.py
# @Author       : njzy njzy4688@gmail.com
# @Date         : 2024-09-14 22:19:14
# @LastEditors  : njzy njzy4688@gmail.com
# @LastEditTime : 2024-10-05 17:05:21
###
from .db import db
from .notice import Notice
from .oa import OA
from .permission_group import PermissionGroup
from .permission_node import PermissionNode
from .role import Teacher, Student
from .school_class import SchoolClass
from .subject import Subject
from .time_slot import TimeSlotTable, Activity
from .transaction_detail import TransactionDetail
from .user import User
