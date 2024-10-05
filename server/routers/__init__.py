#!/usr/bin/env python
# coding=utf-8
###
# @FilePath     : /school_backend/server/routers/__init__.py
# @Author       : njzy njzy4688@gmail.com
# @Date         : 2024-09-10 23:58:15
# @LastEditors  : njzy njzy4688@gmail.com
# @LastEditTime : 2024-10-05 17:19:41
###
from fastapi import FastAPI


def include_routers(app: FastAPI):
    from . import transaction, user, oa, role

    app.include_router(oa.api)
    app.include_router(role.api)
    app.include_router(transaction.api)
    app.include_router(user.api)
