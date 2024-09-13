from pony.orm import Required, db_session

from .db import db
from .permission_group import PermissionGroup


class PermissionNode(db.Entity):
    permission = Required(str)
    value = Required(bool)
    owner = Required(PermissionGroup)

    @classmethod
    @db_session
    def instance(cls, permission, value, owner):
        result = cls.get(permission=permission, owner=owner)
        if result is None:
            if value is None:
                raise ValueError
            return cls(permission=permission, value=value, owner=owner)
        if value is not None:
            result.value = value
        return result
