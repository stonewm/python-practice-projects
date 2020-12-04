import pyodbc
import unittest

conn = pyodbc.connect(DSN="msaccess_employees")
cursor = conn.cursor()


class TestPyOdbc(unittest.TestCase):

    def test_select(self):
        cursor.execute("select * from employees")

        result = cursor.fetchall()  # result为list类型
        for item in result:
            print(item)  # item为pyodbc.Row类型

    def test_insert(self):
        sql = """
            INSERT INTO employees ( EMP_ID, FIRST_NAME, LAST_NAME, GENDER, 
                                    AGE, EMAIL, PHONE_NR, EDUCATION, MARITAL_STAT,NR_OF_CHILDREN )
            VALUES ('9001', 'Stone', 'Wang', 'Male', 18, 'stone@126.com', '138xxx', 'Bachelor', 'Married', 2 ); 
        """
        cursor.execute(sql)
        conn.commit()

    def test_update(self):
        sql = "update employees set AGE=20 where EMP_ID=9001"
        cursor.execute(sql)
        conn.commit()

    def test_delete(self):
        cursor.execute("delete from employees where EMP_ID=9001")

    def test_sql_with_parameter(self):
        sql = "select * from employees where EMP_ID=?"
        cursor.execute(sql, ['1001'])

        print(cursor.fetchone())


if __name__ == "__main__":
    unittest.main()
