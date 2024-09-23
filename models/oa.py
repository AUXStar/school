from pony.orm import Required, db_session, sum, Set, Optional,Json
from decimal import Decimal
from time import time
from enum import Enum
from .db import db



class OA_type(Enum):
    Leave=0
    Money=1


class OA(db.Entity):
    name = Required(str)
    details = Required(Json)
    from_user = Set('User')
    to_user = Set("User")
    type = Required(OA_type)
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
