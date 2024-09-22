from pony.orm import Required, db_session, sum, Set, Optional
from decimal import Decimal
from time import time
from .db import db



class SchoolClass(db.Entity):
    name = Required(str)
    grade = Required(int)
    number = Required(int)
    students = Set("Student")
    teachers = Set("Teacher")
    main_teacher = Required("Teacher",reverse='main_school_class')
    transactions = Set("TransactionDetail")
    time_slot_table = Optional("TimeSlotTable")
