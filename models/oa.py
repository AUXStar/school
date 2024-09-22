from pony.orm import Required, db_session, sum, Set, Optional,Json
from decimal import Decimal
from time import time
from .db import db



class OA(db.Entity):
    name = Required(str)
    details = Required
    from_user = Set('User')
    to_user = Set("User")
    type = Required(int)
    result = Required(int) #0 pending 1 adopt -1 reject

    # result = Required(Json)
    # """
    # {
    #   "to":[
    #   {
    #     "result":
    #   },
    #   {}
    #   ]
    # }
    # """
