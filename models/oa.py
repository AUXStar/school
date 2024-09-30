from pony.orm import Required, db_session, sum, Set, Optional,Json
from decimal import Decimal
from time import time
from enum import Enum
from .db import db



class OA(db.Entity):
    name = Required(str)
    create_timestamp = Required(int,default=lambda:int(time()))
    result_timestamp = Required(int,default=0)
    details = Required(Json)
    from_user = Set('User')
    to_user = Set("User")
    result = Required(int)
    
    #0 pending 1 adopt -1 reject

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
