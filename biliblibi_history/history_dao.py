
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import BiliHistory

engine = create_engine("sqlite:///history.db3", echo=False)
session = sessionmaker(bind=engine)()

def is_url_exists(view_time):
    """根据浏览的时间戳判断记录是否存在"""
    item = session.query(BiliHistory).filter(BiliHistory.view_at==view_time).first()
    return item != None


def create_url_info(url):
    url = BiliHistory(
        title = url.get("title"),

        business = url.get("business"),
        bvid = url.get("bvid"),
        cid = url.get("cid"),
        epid = url.get("epid"),
        oid = url.get("oid"),
        page = url.get("page"),
        part = url.get("part"),
        dt = url.get("dt"),

        author_name = url.get("author_name"),
        videos = url.get("videos"),
        is_fav  = url.get("is_fav"),
        tag_name = url.get("tag_name"),
        view_at = url.get("view_at"),
        progress = url.get("progress"),
        show_title = url.get("show_title"),
        cover =url.get("cover"),
        uri = url.get("uri")
    )

    session.add(url)
    session.commit()
    session.close()


