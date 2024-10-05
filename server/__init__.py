#!/usr/bin/env python
# coding=utf-8
###
# @FilePath     : /school_backend/server/__init__.py
# @Author       : njzy njzy4688@gmail.com
# @Date         : 2024-09-10 23:50:14
# @LastEditors  : njzy njzy4688@gmail.com
# @LastEditTime : 2024-10-05 17:05:34
###
from fastapi import FastAPI, HTTPException, Depends
from starlette.middleware.sessions import SessionMiddleware
from utils.permission import permission_depends
import sys
import os

from models import User


from utils import database, instance_tools


def create_app(instance_dir=None, base_dir=None):
    sys.path.append(
        os.path.abspath(os.path.join(os.path.split(os.path.abspath(__file__))[0], ".."))
    )
    instance_tools.init_instance("instance1", base_dir)

    database.init_db()
    app = FastAPI(title="school_backend")
    app.add_middleware(SessionMiddleware, secret_key="asdf")
    from .routers import include_routers

    include_routers(app)

    @app.get("/s")
    def s(user: User = permission_depends("user")):
        return {"a": user.username}

    return app
