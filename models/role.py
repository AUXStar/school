from pony.orm import Required, db_session, sum, Set, Optional
from decimal import Decimal
from time import time
from .db import db


class Teacher(db.Entity):
    user=Required("User")
    subject=Set("Subject")
    school_class=Set("SchoolClass")
    main_school_class=Optional('SchoolClass')
    

class Student(db.Entity):
    user=Required("User")
    school_class=Set("SchoolClass")
    
