import json
import requests
import time
from history_dao import create_url_info, is_url_exists


def get_response_json(url, req_headers):
    """根据url获取json格式的response文本"""
    resp = requests.get(url, headers=req_headers)
    return json.loads(resp.text)


class BiliHistory(object):

    def __init__(self, cookie_file):
        self.base_url = "https://api.bilibili.com/x/web-interface/history/cursor"
        self.cookie = self._get_cookie_content(cookie_file)
        self.request_headers = self._set_req_headers()

    def _get_cookie_content(self, cookie_file):
        """从cookies.txt中读取cookie"""

        with open(cookie_file, 'r') as fp:
            cookies = fp.read()
            return cookies

    def _set_req_headers(self):
        """设置请求头：1)模拟浏览器；2)提供cookie"""

        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Connection": "keep-alive",
            "Cookie": self.cookie,
            "Host": "api.bilibili.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50"
        }

        return headers

    def _get_history(self, max, view_at, business):
        """根据url以及查询字符串中三个参数，获取20个历史记录，
        history_list: 为包含dict的列表，每一个list是一个历史记录
        cursor: 下一个请求的cursor信息
        """

        url = self.base_url + \
            f"?max={max}&view_at={view_at}&business={business}"
        resp = get_response_json(url, self.request_headers)
        history_list = resp.get("data").get("list")
        next_cursor = resp.get("data").get("cursor")

        return history_list, next_cursor

    def get_all_history(self):
        """获取所有的的浏览历史记录"""

        histories = []

        max = 0
        view_at = 0
        business = ''
        ps = 20

        while(ps != 0):
            history, cursor = self._get_history(max, view_at, business)
            max = cursor.get("max")
            view_at = cursor.get("view_at")
            business = cursor.get("business")
            ps = cursor.get("ps")

            for item in history:
                histories.append(item)
            time.sleep(0.1)

        return histories

    def save_db(self):
        """保存到sqlite3数据库"""

        histories = self.get_all_history()
        for item in histories:
            history = item.get("history")
            view_time = item.get("view_at")

            # 如果记录不在数据库中，则新增记录
            if is_url_exists(view_time) == False:
                url_content = {
                    "title": item.get("title"),

                    "business": history.get("business"),
                    "bvid": history.get("bvid"),
                    "cid": history.get("cid"),
                    "epid": history.get("epid"),
                    "oid": history.get("oid"),
                    "page": history.get("page"),
                    "part": history.get("part"),
                    "dt": history.get("dt"),

                    "author_name": item.get("author_name"),
                    "videos": item.get("videos"),
                    "is_fav": item.get("is_fav"),
                    "tag_name": item.get("tag_name"),
                    "view_at": item.get("view_at"),
                    "progress": item.get("progress"),
                    "show_title": item.get("show_title"),
                    "cover": item.get("cover"),
                    "uri": item.get("uri")
                }
                create_url_info(url_content)


if __name__ == '__main__':
    # 将浏览的历史记录保存到数据库
    bili = BiliHistory("cookies.txt")
    bili.save_db()
