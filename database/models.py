from pony.orm import Database, Required, db_session, sum
from decimal import Decimal
from time import time

db = Database()

# class Teacher(db.Entity):


# class SchoolClass(db.Entity):
#     name=Required(str)
#     grade=Required(int)
#     class_=Required(int)


class TransactionDetail(db.Entity):
    detail = Required(str,500)
    money = Required(Decimal,10,2)
    timestamp = Required(int,default=lambda:int(time()))

    @classmethod
    @db_session
    def total(cls):
        return sum(td.money for td in cls)


def connect_db(db:Database,db_connect:dict=None):
    db.bind(**db_connect)
    db.generate_mapping(create_tables=True)
