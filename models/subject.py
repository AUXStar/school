#!/usr/bin/env python
# coding=utf-8
###
# @FilePath     : /school_backend/models/subject.py
# @Author       : njzy njzy4688@gmail.com
# @Date         : 2024-09-19 13:04:12
# @LastEditors  : njzy njzy4688@gmail.com
# @LastEditTime : 2024-10-05 17:06:33
###
from typing import Self

from pony.orm import Required, Set, db_session

from .db import db


class Subject(db.Entity):
    name = Required(str, index=True)
    teacher = Set("Teacher")
    tags = Set(lambda: SubjectTag)
    activities = Set("Activity")


class SubjectTag(db.Entity):
    name = Required(str, unique=True, index=True)
    subject = Set(Subject)

    @classmethod
    def instance(cls, name: str):
        obj = cls.get(name=name)
        if not obj:
            obj = cls(name=name)
        return obj
