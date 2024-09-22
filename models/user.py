from pony.orm import Required, db_session, sum, Set, Optional
from decimal import Decimal
from time import time
from .db import db


class User(db.Entity):
    username = Required(str, index=True)
    password = Required(str)
    realname = Required(str)
    nickname = Optional(str)
    id_card = Required(str)
    class_teacher = Optional("Teacher")
    class_student = Optional("Student")

    gender = Required(int) #0male 1female

    oa_from = Set('OA',reverse='from_user')
    oa_to = Set('OA',reverse='to_user')

    permission_groups = Set("PermissionGroup", index=True)

    @classmethod
    def from_id(cls, uid=-1):
        obj = cls.get(id=uid)
        if not obj:
            if not (obj := cls.get(id=-1)):
                obj = cls(
                    id=-1,
                    username="Guest",
                    password="GUEST_NO_PASSWORD",
                    realname="游客",
                )
        return obj
