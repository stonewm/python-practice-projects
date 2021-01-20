# coding: utf-8
from sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import Table

engine = create_engine("sqlite:///testdb.db")
Base = declarative_base()
metadata = Base.metadata
metadata.bind = engine

class Employee(Base):
    __table__ = Table("employees", metadata, autoload=True)
