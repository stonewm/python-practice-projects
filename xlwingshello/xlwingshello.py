import xlwings as xw
import pandas as pd
from sqlalchemy import create_engine


def hello_xlwings():
    wb = xw.Book.caller()
    wb.sheets[0].range("A1").value = "Hello xlwings!"


@xw.func
def hello(name):
    return "hello {0}".format(name)


def write_hello():
    wb = xw.Book()  # create a new workbook
    sht = wb.sheets[0]  # Open worksheet
    sht.range("A1").value = "Hello, xlwings!"  # write hello


def upload_employees():
    url = "mysql+pymysql://root:w123456@localhost:3306/stonetest?charset=utf8"
    engine = create_engine(url)

    emp_data = pd.read_sql("select * from emp_master", engine)

    wb = xw.Book.caller()
    wb.sheets[0].range("A2").options(index=True).value = emp_data


# write_hello()