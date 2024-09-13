from pony.orm import select, exists, count,db_session
from argon2 import PasswordHasher
from argon2.exceptions import InvalidHash, VerifyMismatchError
from pydantic import BaseModel, constr, conint, EmailStr, field_validator
from fastapi import APIRouter, HTTPException, Request

from models import user, permission_group

api = APIRouter(prefix='/user')

argon = PasswordHasher(time_cost=10)


class RegisterData(BaseModel):
    username: constr(min_length=3, max_length=16,
                     pattern=r'^[\u4e00-\u9fa5a-zA-Z0-9-_]+$') # type: ignore
    password: constr(min_length=8) # type: ignore
    realname: str

    @classmethod
    @field_validator("password")
    def password_strength_test(cls, v: str) -> str:
        ...
        return v


@api.post("/register")
def register(data:RegisterData,request:Request):
    if data.username == "Guest":
        raise HTTPException(403,{"success": False, "reason": "User already exists. ", "id": -1})
    with db_session:
        # noinspection PyTypeChecker
        if exists(u for u in user.User if u.username == data.username):
            raise HTTPException(403,{"success": False, "reason": "User already exists. ", "id": -1})

        hashed_password = argon.hash(data.password)
        user_group = permission_group.PermissionGroup.instance("user", 0)
        register_user = user.User(
            username=data.username,
            password=hashed_password,
            realname=data.realname,
            permission_groups=[user_group]
        )
        register_user.flush()
        request.session['id'] = register_user.id
        return {"success": True, "reason": "", 'id': register_user.id}



class LoginData(BaseModel):
    login: constr(min_length=3) | EmailStr # type: ignore
    password: constr(min_length=8) # type: ignore

@api.post("/login")
def login(data:LoginData,request:Request):
    with db_session:
        login_user: user.User = select(
            u for u in user.User if u.username == data.login).get()
        if login_user is None:
            raise HTTPException(403,{"success": False, "reason": "Wrong login/password. ", "id": -1})
        try:
            argon.verify(login_user.password, data.password)
        except (InvalidHash, VerifyMismatchError):
            raise HTTPException(403,{"success": False, "reason": "Wrong login/password. ", "id": -1})
        
        request.session["id"] = login_user.id
        return {"success": True, "reason": "", "id": login_user.id}


@api.get("/logout")
def logout(request:Request):
    request.session.pop('id', None)
    return {"success": True, 'data': {} }
