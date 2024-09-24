from pony.orm import select, exists, count, db_session
from argon2 import PasswordHasher
from argon2.exceptions import InvalidHash, VerifyMismatchError
from pydantic import BaseModel, constr, conint, EmailStr, field_validator
from fastapi import APIRouter, HTTPException, Request

from models import User, PermissionGroup

api = APIRouter(prefix="/user")

argon = PasswordHasher(time_cost=10)


class RegisterData(BaseModel):
    username: constr(
        min_length=3, max_length=25, pattern=r"^[\u4e00-\u9fa5a-zA-Z0-9-_]+$"
    )  # type: ignore
    password: constr(min_length=8, max_length=32)  # type: ignore
    realname: str
    id_card: str
    phone: str

    @classmethod
    @field_validator("password")
    def password_strength_test(cls, v: str) -> str:
        ...
        return v
    
    @classmethod
    @field_validator("id_card")
    def id_card_test(cls, v: str) -> str:
        ...
        return v
    
    @classmethod
    @field_validator("phone")
    def phone_test(cls, v: str) -> str:
        ...
        return v


@api.post("/register")
async def register(data: RegisterData, request: Request):
    if data.username == "Guest":
        raise HTTPException(
            403, {"success": False, "reason": "User already exists. ", "id": -1}
        )
    with db_session:
        # noinspection PyTypeChecker
        if exists(u for u in User if u.username == data.username):
            raise HTTPException(
                403, {"success": False, "reason": "User already exists. ", "id": -1}
            )

        hashed_password = argon.hash(data.password)
        user_group = PermissionGroup.instance("user", 0)
        register_user = User(
            username=data.username,
            password=hashed_password,
            realname=data.realname,
            id_card=data.id_card,
            phone=data.phone,
            gender=1,
            permission_groups=[user_group],
        )
        register_user.flush()
        request.session["id"] = register_user.id
        return {"success": True, "reason": "", "id": register_user.id}


class LoginData(BaseModel):
    username: constr(min_length=3, max_length=25) | EmailStr  # type: ignore
    password: constr(min_length=8, max_length=32)  # type: ignore


@api.post("/login")
async def login(data: LoginData, request: Request):
    with db_session:
        login_user: User = select(u for u in User if u.username == data.username).get()
        if login_user is None:
            raise HTTPException(
                403, {"success": False, "reason": "Wrong login/password. ", "id": -1}
            )
        try:
            argon.verify(login_user.password, data.password)
        except (InvalidHash, VerifyMismatchError):
            raise HTTPException(
                403, {"success": False, "reason": "Wrong login/password. ", "id": -1}
            )

        request.session["id"] = login_user.id
        return {"id": login_user.id}


@api.get("/logout")
async def logout(request: Request):
    request.session.pop("id", None)
    return {"success": True}


@api.get("/self_info")
async def self_info(request:Request):
    with db_session:
        user = User.from_id(request.session.get("id", -1))
        return {
            "username": user.username,
            "realname": user.realname,
            "permission_groups": list(select(pg.name for pg in user.permission_groups)[:])
        }