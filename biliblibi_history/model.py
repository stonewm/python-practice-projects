# coding: utf-8
from sqlalchemy import BigInteger, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata

class BiliHistory(Base):
    __tablename__ = 'bili_history'

    id=Column(Integer, primary_key=True, autoincrement=True)
    title = Column(Text)
    business = Column(Text(50))
    bvid = Column(Text(20))
    cid = Column(Text(20))
    dt = Column(Integer)
    epid = Column(Integer)
    oid = Column(Integer)
    page = Column(Integer)
    part = Column(Text(255))
    author_name = Column(Text(50))
    videos = Column(Integer)
    is_fav = Column(Integer)
    tag_name = Column(Text(50))
    view_at = Column(BigInteger)
    progress = Column(Integer)
    show_title = Column(Text(255))
    cover = Column(Text(255))
    uri = Column(Text)
    url = Column(Text)


if __name__ == '__main__':
    from sqlalchemy import create_engine
    engine = create_engine("sqlite:///history.db3", echo=False)
    Base.metadata.create_all(bind=engine)
