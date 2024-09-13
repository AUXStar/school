from pony.orm import Required, db_session, sum
from decimal import Decimal
from time import time

from .db import db

class TransactionDetail(db.Entity):
    class_=Required("SchoolClass")
    detail = Required(str,500)
    money = Required(Decimal,10,2)
    timestamp = Required(int,default=lambda:int(time()))

    @classmethod
    @db_session
    def total(cls):
        return sum(td.money for td in cls)

