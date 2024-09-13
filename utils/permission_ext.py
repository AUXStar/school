from typing import Callable, TypeVar
from functools import wraps


from models import User
from permission import check_permission

T = TypeVar("T")
F = TypeVar("F", bound=Callable)


def require_permission_fun(permission_id: str, reason: str = "Access Denied. ") -> Callable[[F], F]:
    def closure_decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args, **kwargs) -> T:
            if not check_permission(User.from_session(session), permission_id):
                return Response(response=json.dumps(
                    {"success": False,
                     "reason": reason,
                     "need_permission": permission_id,
                     "user": User.from_session(session).username}), status=403,
                    mimetype='application/json')
            return func(*args, **kwargs)

        return wrapper

    return closure_decorator


def require_permission_blueprint(bp: Blueprint, permission_id: str, reason: str = "Access Denied. ") -> None:
    @bp.before_request
    def before_request():
        if not check_permission(User.from_session(session), permission_id):
            abort(Response(response=json.dumps(
                {"success": False,
                 "reason": reason,
                 "need_permission": permission_id,
                 "user": User.from_session(session).username
                 }), status=403, mimetype='application/json'))
