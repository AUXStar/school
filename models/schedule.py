from typing import Self

from pony.orm import Required, Set, db_session

from .db import db


class Schedule(db.Entity):
    ...