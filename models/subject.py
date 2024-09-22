from typing import Self

from pony.orm import Required, Set, db_session

from .db import db


class Subject(db.Entity):
    name = Required(str, unique=True, index=True)
    teacher = Required("Teacher")
    tags = Set(lambda:SubjectTag)
    activities = Set("Activity")


class SubjectTag(db.Entity):
    name=Required(str, unique=True, index=True)
    subject=Set(Subject)

    @classmethod
    def instance(cls, name:str):
        obj = cls.get(name=name)
        if not obj:
            obj = cls(name=name)
        return obj
