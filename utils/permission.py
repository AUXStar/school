from typing import Callable, TypeVar
from functools import wraps

from queue import Queue

from models import user
from pony.orm import select,db_session
from fastapi import Depends,HTTPException,Request


T = TypeVar("T")
F = TypeVar("F", bound=Callable)


def permission_depends(permission_id: str, reason: str = "Access Denied. ") -> Callable[[F], F]:
    def closure_decorator(request:Request) -> F:
        with db_session:
            current_user = user.User.from_id(request.session.get('id',-1))
            if not check_permission(current_user, permission_id):
                return HTTPException(403,{"success": False,
                        "reason": reason,
                        "need_permission": permission_id,
                        "user": current_user.username})
            return current_user
    return closure_decorator

def check_permission(user: user.User, permission:str):
    queue = Queue()
    weight = float("-inf")
    value = False
    for group in user.permission_groups:
        queue.put(group)
    while not queue.empty():
        group = queue.get()
        for g in group.parents:
            queue.put(g)
        if group.weight < weight:
            continue
        values = select(node.value for node in group.nodes if node.permission == permission)
        for v in values:
            value = v
            weight = group.weight
    return value
