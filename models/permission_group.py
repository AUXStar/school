#!/usr/bin/env python
# coding=utf-8
###
# @FilePath     : /school_backend/models/permission_group.py
# @Author       : njzy njzy4688@gmail.com
# @Date         : 2024-09-14 22:19:14
# @LastEditors  : njzy njzy4688@gmail.com
# @LastEditTime : 2024-10-05 17:09:58
###
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
