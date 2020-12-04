from ADOWrapper.ado_command import CommandWrapper
from ADOWrapper.ado_connection import ConnectionWrapper
from ADOWrapper.ado_recordset import RecordSetWrapper
from msaccess_db_file_path import get_access_db_file
import unittest

# 连接MS Access数据库
conn_str = "Provider=Microsoft.ACE.OLEDB.12.0;Data Source=%s;" % get_access_db_file()
conn = ConnectionWrapper(conn_str).get_connection()


class TestAdoWrapper(unittest.TestCase):
    def test_insert(self):
        sql = """
                INSERT INTO employees 
                       ( EMP_ID, FIRST_NAME, LAST_NAME, GENDER, AGE, EMAIL, PHONE_NR, 
                         EDUCATION, MARITAL_STAT, NR_OF_CHILDREN)
                VALUES ('9001', 'Stone', 'Wang', 'Male', 18, 'stone@126.com', '138xxx', 'Bachelor', 'Married', 2 ); 
              """
        CommandWrapper.execute(conn, sql)

    def test_update(self):
        sql = "UPDATE employees SET AGE=20 WHERE EMP_ID=9001"
        CommandWrapper.execute(conn, sql)

    def test_delete(self):
        CommandWrapper.execute(conn, "DELETE FROM employees WHERE EMP_ID=9001")

    def test_query(self):
        result = RecordSetWrapper.query(conn, "SELECT * FROM employees")
        for record in result:
            print(record)

    def test_query_table(self):
        result = RecordSetWrapper.query(conn, "employees")
        for record in result:
            print(record)

    def test_export_to_excel(self):
        rst = RecordSetWrapper.get_recordset(conn, "select * from employees where EMP_ID<1020;")
        RecordSetWrapper.to_excel(rst, "D:/employee_output.xlsx")


if __name__ == "__main__":
    unittest.main()
