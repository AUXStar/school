#!/usr/bin/env python
# coding=utf-8
###
# @FilePath     : /school_backend/models/permission_node.py
# @Author       : njzy njzy4688@gmail.com
# @Date         : 2024-09-14 22:19:14
# @LastEditors  : njzy njzy4688@gmail.com
# @LastEditTime : 2024-10-05 17:06:54
###
from pony.orm import Required, db_session

from .db import db
from .permission_group import PermissionGroup


class PermissionNode(db.Entity):
    permission = Required(str, index=True)
    value = Required(bool)
    owner = Required(PermissionGroup)

    @classmethod
    @db_session
    def instance(cls, permission: str, value: bool, owner: PermissionGroup):
        result = cls.get(permission=permission, owner=owner)
        if result is None:
            if value is None:
                raise ValueError
            return cls(permission=permission, value=value, owner=owner)
        if value is not None:
            result.value = value
        return result
