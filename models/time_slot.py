from typing import Self

from pony.orm import Required, Set, db_session, Optional
from datetime import time

from .db import db



class TimeSlotWeek(db.Entity):
    week_single=Required(int) # 0none 1single 2double
    week_day=Required(int) #1-7
    time_slot=Set(lambda:TimeSlot)
    
    @classmethod
    def instance(cls, 
        week_single:int,
        week_day:int,
        time_slot:list[tuple[time,time]]):
        obj = cls.get(name=name)
        if not obj:
            obj = cls(name=name)
        return obj



class TimeSlot(db.Entity):
    week=Required(TimeSlotWeek)
    start_time=Required(time)
    end_time=Required(time)
    