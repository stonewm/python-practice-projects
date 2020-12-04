"""
原生的|RecordSet具备CRUD功能，本示例说明其用法
"""

from ADOWrapper.ado_connection import ConnectionWrapper
from ADOWrapper.ado_recordset import RecordSetWrapper
from ADOWrapper.adoconstants import *
from win32com.client import Dispatch
from msaccess_db_file_path import get_access_db_file
import unittest

# 连接MS Access数据库
conn_str = "Provider=Microsoft.ACE.OLEDB.12.0;Data Source=%s;" % get_access_db_file()
conn = ConnectionWrapper(conn_str).get_connection()


class TestRecordSet(unittest.TestCase):

    def test_list_employees(self):
        rst = RecordSetWrapper.get_recordset(conn, "select * from employees")
        if rst.BOF and rst.EOF:
            return

        rst.MoveFirst()
        while not rst.EOF:
            for idx in range(0, rst.Fields.Count):
                print(rst.Fields(idx), end=",")
            print()
            rst.MoveNext()

        rst.Close()
        conn.Close()

    def test_create_employee(self):
        rst = Dispatch("ADODB.Recordset")
        conn.Open()
        rst.Open('employees', conn, adOpenKeyset, adLockOptimistic)

        try:
            rst.AddNew()
            rst.Fields("EMP_ID").Value = '9002'
            rst.Fields("FIRST_NAME").Value = 'Stone'
            rst.Fields("LAST_NAME").Value = "Wang"
            rst.Update()

            print('新增记录成功!')
        except Exception as ex:
            print(ex)
            for err in conn.Errors:
                print(err)
        finally:
            rst.Close()
            conn.Close()

    def test_modify_employee(self):
        rst = Dispatch("ADODB.Recordset")

        try:
            conn.Open()
            sql = "SELECT * FROM employees WHERE EMP_ID=9002"

            rst.Open(sql, conn, adOpenKeyset, adLockOptimistic)
            if not rst.EOF:
                rst.Fields('AGE').Value = 18
                rst.Update()

                print('修改成功!')
        except Exception as ex:
            print(ex)
            for err in conn.Errors:
                print(err)
        finally:
            rst.Close()
            conn.Close()

    def test_delete_employee(self):
        rst = Dispatch("ADODB.Recordset")

        conn.Open()
        sql = "SELECT * FROM employees WHERE EMP_ID=9002"

        try:
            # IMPORTANT: client cursor should be used for deletion
            rst.CursorLocation = adUseClient
            rst.Open(sql, conn, adOpenKeyset, adLockOptimistic)

            if not rst.EOF:
                rst.Delete(1)  # deleter first row
                print('删除成功!')
            else:
                print('没有找到记录!')
        except Exception as ex:
            print(ex)
            for err in conn.Errors:
                print(err)
        finally:
            rst.Close()
            conn.Close()


if __name__ == '__main__':
    unittest.main()
