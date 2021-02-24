from sqlalchemy import create_engine
import unittest

engine = create_engine('sqlite:///testdb.db')


class TestRawSql(unittest.TestCase):
    def test_delete(self):
        with engine.connect() as conn:
            conn.execute('delete from employees')

    def test_select_statement(self):
        with engine.connect() as conn:
            result_proxy = conn.execute("select * from employees")  # 返回值为ResultProxy类型
            result = result_proxy.fetchall()

            for item in result:
                print(item)

    def test_parameter_method1(self):
        with engine.connect() as conn:
            conn.execute(
                """INSERT INTO employees
                       (EMP_ID, FIRST_NAME, LAST_NAME, GENDER, 
                        AGE, EMAIL, PHONE_NR,EDUCATION, 
                        MARITAL_STAT, NR_OF_CHILDREN)
                   VALUES (?,?,?,?,?,?,?,?,?,?);
                """,
                ('9002', 'Stone2', 'Wang', 'M', 20,
                 'stone@gmail.com', '138xxx', 'Bachelor', 'Single', 0)
            )

    def test_parameter_method2(self):
        with engine.connect() as conn:
            conn.execute(
                """INSERT INTO employees
                       (EMP_ID, FIRST_NAME, LAST_NAME, GENDER, 
                        AGE, EMAIL, PHONE_NR, EDUCATION, 
                        MARITAL_STAT, NR_OF_CHILDREN)
                   VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10);
                """,
                ('9003', 'Stone3', 'Wang', 'M', 20, 'stone@gmail.com',
                 '138xxx', 'Bachelor', 'Single', 0)
            )

    def test_insert_multiple_rows(self):
        with engine.connect() as conn:
            values = [
                ('9004', 'Stone4', 'Wang', 'M', 20, 'stone@gmail.com', '138xxx', 'Bachelor', 'Single', 0),
                ('9005', 'Stone5', 'Wang', 'M', 20, 'stone@gmail.com', '138xxx', 'Bachelor', 'Single', 0),
                ('9006', 'Stone6', 'Wang', 'M', 20, 'stone@gmail.com', '138xxx', 'Bachelor', 'Single', 0)
            ]
            conn.execute(
                """INSERT INTO employees
                       (EMP_ID, FIRST_NAME, LAST_NAME, GENDER, 
                        AGE, EMAIL, PHONE_NR, EDUCATION, 
                        MARITAL_STAT, NR_OF_CHILDREN)
                   VALUES (?,?,?,?,?,?,?,?,?,?);
                """, values)

    def test_txn(self):
        conn = engine.connect()
        with conn.begin() as txn:
            conn.execute(
                """INSERT INTO employees
                       (EMP_ID, FIRST_NAME, LAST_NAME, GENDER, AGE, EMAIL, PHONE_NR,
                        EDUCATION, MARITAL_STAT, NR_OF_CHILDREN)
                   VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10);
                """,
                ('9007', 'Stone7', 'Wang', 'M', 20, 'stone@gmail.com', '138xxx', 'Bachelor', 'Single', 0)
            )

            txn.commit()
        conn.close()

    def test_exception(self):
        conn = engine.connect()
        try:
            conn.execute('select * from employeess')
        except Exception as ex:
            print(ex)
        finally:
            conn.close()


if __name__ == '__main__':
    unittest.main()
