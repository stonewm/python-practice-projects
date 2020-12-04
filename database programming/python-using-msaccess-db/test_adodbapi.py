import adodbapi
import os
import unittest


def get_current_dir():
    """
    获取当前文件夹
    """
    return os.path.dirname(os.path.abspath(__file__))


db_file_path = get_current_dir() + r'\db\Employees.accdb'
conn_str = "Provider=Microsoft.ACE.OLEDB.12.0;Data Source=%s;" % db_file_path

conn = adodbapi.connect(conn_str)
cursor = conn.cursor()


class TestAdodbapi(unittest.TestCase):

    def test_select(self):
        cursor.execute("select * from employees;")

        result = cursor.fetchall()  # result为adodbpai.apibase.SQLRows类型
        for item in result:
            print(item)             # itemadodbpai.apibase.SQLRow类型

    def test_insert(self):
        sql = """
            INSERT INTO employees ( EMP_ID, FIRST_NAME, LAST_NAME, 
                                    GENDER, AGE, EMAIL, PHONE_NR, EDUCATION, MARITAL_STAT, NR_OF_CHILDREN)
            VALUES ('9001', 'Stone', 'Wang', 'Male', 18, 'stone@126.com', '138xxx', 'Bachelor', 'Married', 2); 
        """
        cursor.execute(sql)
        conn.commit()

    def test_update(self):
        sql = "update employees set AGE=20 where EMP_ID=9001"
        cursor.execute(sql)
        conn.commit()

    def test_delete(self):
        cursor.execute("delete from employees where EMP_ID=9001")

    def test_sql_with_paramter(self):
        sql = "select * from employees where EMP_ID=?"
        cursor.execute(sql, (1001,))

        print(cursor.fetchone())


if __name__ == "__main__":
    unittest.main()
