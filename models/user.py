from pony.orm import Required, db_session, sum, Set, Optional
from decimal import Decimal
from time import time
from .db import db


class User(db.Entity):
    username = Required(str)
    password = Required(str)
    realname = Required(str)
    nickname = Optional(str)
    class_teacher = Optional(lambda: SchoolClass, reverse="teachers")
    class_student = Optional(lambda: SchoolClass, reverse="students")

    permission_groups = Set("PermissionGroup")

    @classmethod
    def from_id(cls, uid=-1):
        user = cls.get(id=uid)
        if not user:
            if not (user := cls.get(id=-1)):
                user = cls(
                    id=-1,
                    username="Guest",
                    password="GUEST_NO_PASSWORD",
                    realname="游客",
                )
        return user


# class Teacher(db.Entity):


class SchoolClass(db.Entity):
    name = Required(str)
    grade = Required(int)
    class_ = Required(int)
    students = Set(User)
    teachers = Set(User)
    transactions = Set("TransactionDetail")
