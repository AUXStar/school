from typing import Self

from pony.orm import Required, Set, db_session, Optional, select
from datetime import time

from .db import db

"""
先有一个通用的一般性的表，然后让临时安排覆盖在这里
每个部的每周时间安排是一样的
时间表下面分有每一天的表
每一天的表有每一天的内容
分散的存每一节课？
"""


class Activity(db.Entity):
    time_slot_time = Required(lambda: TimeSlotTime)  # 时间
    time_slot_week = Required(lambda: TimeSlotWeek)  # 星期
    time_slot_table = Required(lambda: TimeSlotTable)  # 集成进表
    subject = Optional("Subject")
    detail = Optional(str)

    @classmethod
    def instance(cls, time_slot_time: int, time_slot_week: int,time_slot_table):
        obj = cls.get(week_single=week_single, week_day=week_day)
        if not obj:
            obj = cls(week_single=week_single, week_day=week_day)
        return obj


class TimeSlotTable(db.Entity):  # 整个的表
    school_class = Required("SchoolClass")
    activities = Set(Activity)


class TimeSlotWeek(db.Entity):  # 单天
    week_single = Required(int)  # 0none 1single 2double
    week_day = Required(int)  # 1-7
    activities = Set(Activity)

    @classmethod
    def instance(cls, week_single: int, week_day: int):
        obj = cls.get(week_single=week_single, week_day=week_day)
        if not obj:
            obj = cls(week_single=week_single, week_day=week_day)
        return obj


class TimeSlotTime(db.Entity):  # 单行
    start_time = Required(time)
    end_time = Required(time)
    activities = Set(Activity)

    @classmethod
    def instance(cls, start_time: time, end_time: time):
        obj = cls.get(start_time=start_time, end_time=end_time)
        if not obj:
            obj = cls(start_time=start_time, end_time=end_time)
        return obj
