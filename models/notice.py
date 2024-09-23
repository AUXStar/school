from pony.orm import Required, db_session, sum, Set, Optional,Json
from decimal import Decimal
from time import time
from .db import db



class Notice(db.Entity):
    title = Required(str)
    details = Required(Json)
    from_user = Set('User')
    to_user = Set("User")
    type = Required(int)
    result = Required(int)
