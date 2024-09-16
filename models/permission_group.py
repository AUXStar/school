from typing import Self

from pony.orm import Required, Set, db_session

from .db import db


class PermissionGroup(db.Entity):
    name = Required(str, unique=True, index=True)
    weight = Required(int)
    nodes = Set("PermissionNode")
    members = Set("User")
    parents = Set("PermissionGroup", reverse="children")
    children = Set("PermissionGroup", reverse="parents")

    @classmethod
    @db_session
    def instance(cls, name: str, weight: int = None) -> Self:
        result = cls.get(name=name)
        if result is None:
            if weight is None:
                raise ValueError
            return cls(name=name, weight=weight)
        if weight is not None:
            result.weight = weight
        return result
