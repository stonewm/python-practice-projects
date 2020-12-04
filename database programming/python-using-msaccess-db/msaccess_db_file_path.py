import os


def get_current_dir():
    """
    获取当前文件夹
    """
    return os.path.dirname(os.path.abspath(__file__))


def get_access_db_file():
    return get_current_dir() + '/db/Employees.accdb'
