#!/usr/bin/env python
# coding=utf-8
###
# @FilePath     : /school_backend/utils/database.py
# @Author       : njzy njzy4688@gmail.com
# @Date         : 2024-09-14 22:19:14
# @LastEditors  : njzy njzy4688@gmail.com
# @LastEditTime : 2024-10-05 17:05:27
###
from models.db import db
from utils import instance_tools

def init_db():
    instance = instance_tools.CURRENT_INSTANCE
    db.bind(instance.config.db_connect)
    db.generate_mapping(create_tables=True)