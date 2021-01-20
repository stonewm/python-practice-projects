# coding: utf-8
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from utils import ModelExt

Base = declarative_base()


class User(Base, ModelExt):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    addresses = relationship("Address", backref="user", cascade="all, delete")

class Address(Base, ModelExt):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))


if __name__ == '__main__':
    engine = create_engine("sqlite:///testdb.db")
    Base.metadata.create_all(engine)





