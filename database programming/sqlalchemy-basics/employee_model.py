# coding: utf-8
from sqlalchemy import Column, SmallInteger, Text
from sqlalchemy.ext.declarative import declarative_base
from utils import ModelExt

Base = declarative_base()
metadata = Base.metadata


class Employee(Base, ModelExt):
    __tablename__ = 'employees'

    EMP_ID = Column(SmallInteger, primary_key=True)
    FIRST_NAME = Column(Text(255))
    LAST_NAME = Column(Text(255))
    GENDER = Column(Text(255))
    AGE = Column(SmallInteger)
    EMAIL = Column(Text(255))
    PHONE_NR = Column(Text(255))
    EDUCATION = Column(Text(255))
    MARITAL_STAT = Column(Text(255))
    NR_OF_CHILDREN = Column(SmallInteger)
