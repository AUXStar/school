#!/usr/bin/env python
# coding=utf-8
###
# @FilePath     : /school_backend/server/routers/role.py
# @Author       : njzy njzy4688@gmail.com
# @Date         : 2024-10-05 17:18:54
# @LastEditors  : njzy njzy4688@gmail.com
# @LastEditTime : 2024-10-05 17:24:11
###
from pony.orm import select, exists, count, db_session
from argon2 import PasswordHasher
from argon2.exceptions import InvalidHash, VerifyMismatchError
from pydantic import BaseModel, constr, conint, EmailStr, field_validator
from fastapi import APIRouter, HTTPException, Request

from models import User, PermissionGroup
from utils.permission import permission_depends

api = APIRouter(prefix="/role")

@api.post('/set_role')
def set_role(user:User=permission_depends('user')):
    user
    return {}
    
