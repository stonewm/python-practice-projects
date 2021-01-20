from sqlalchemy import create_engine, and_, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
from employee_model import Employee
from utils import to_formatted_table

import unittest

engine = create_engine("sqlite:///testdb.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()


class TestSACrud(unittest.TestCase):
    def test_create_emp(self):
        emp = Employee(
            EMP_ID = "9002",
            FIRST_NAME= "Lauren",
            LAST_NAME = "Daigle",
            GENDER = "Female",
            AGE = 20,
            EMAIL = "unknown",
            PHONE_NR = "unknown",
            EDUCATION = "Bachelor",
            NR_OF_CHILDREN = 0
        )
        session.add(emp)
        session.commit()

    def test_modify(self):
        emp = session.query(Employee).filter_by(EMP_ID='9002').first()
        emp.AGE = '21'
        session.commit()

    def test_delete(self):
        emp = session.query(Employee).filter_by(EMP_ID='9002').first()
        session.delete(emp)
        session.commit()


    def test_query_all(self):
        # 对象作参数，返回值类型为 list[Employee_Object]
        employees = session.query(Employee).all()
        print(to_formatted_table(employees))


    def test_query_selected_fields(self):
        # 返回值类型：list[sqlalchemy.util._collections.result]
        employees = session.query(Employee.EMP_ID, Employee.FIRST_NAME, Employee.LAST_NAME).all()
        for emp in employees:
            print(emp)

    def test_query_selected_fields2(self):
        employees = session.query(Employee.EMP_ID, Employee.FIRST_NAME, Employee.LAST_NAME).all()
        for item in employees:
            print(item.EMP_ID, item.FIRST_NAME, item.LAST_NAME)

    def test_query_selected_fields3(self):
        for id, first_name, last_name in session.query(Employee.EMP_ID, Employee.FIRST_NAME, Employee.LAST_NAME):
            print(id, first_name, last_name)

    def test_filtered_query(self):
        emp = session.query(Employee).filter_by(EMP_ID='1001').first()
        print(emp)

    def test_filtered_query2(self):
        emp = session.query(Employee).filter(Employee.EMP_ID == '1001').first()
        print(emp)

    def test_filter_le(self):
        emps = session.query(Employee).filter(Employee.EMP_ID <= '1009').all()
        print(to_formatted_table(emps))

    def test_filter_ne(self):
        emps = session.query(Employee).filter(Employee.EMP_ID != '1001').all()
        print(to_formatted_table(emps))

    def test_filter_like(self):
        emps = session.query(Employee).filter(Employee.EMP_ID.like('%9')).all()
        print(to_formatted_table(emps))

    def test_filter_in(self):
        emps = session.query(Employee).filter(Employee.EDUCATION.in_(['Bachelor', 'Master'])).all()
        print(to_formatted_table(emps))

    def test_filter_notin(self):
        emps = session.query(Employee).filter(~Employee.EDUCATION.in_(['Bachelor', 'Master'])).all()
        print(to_formatted_table(emps))

    def test_filter_isnull(self):
        emps = session.query(Employee).filter(Employee.MARITAL_STAT == None).all()
        print(to_formatted_table(emps))

    def test_filter_isnotnull(self):
        emps = session.query(Employee).filter(Employee.MARITAL_STAT != None).all()
        print(to_formatted_table(emps))

    def test_filter_and(self):
        emps = session.query(Employee).filter(Employee.GENDER=='Female', Employee.EDUCATION=='Bachelor').all()
        print(to_formatted_table(emps))

    def test_filter_and2(self):
        emps = session.query(Employee).filter(and_(Employee.GENDER=='Female', Employee.EDUCATION=='Bachelor')).all()
        print(to_formatted_table(emps))

    def test_filter_or(self):
        emps = session.query(Employee).filter(or_(Employee.MARITAL_STAT=='Single', Employee.NR_OF_CHILDREN==0)).all()
        print(to_formatted_table(emps))


    def test_get_state(self):
        emp = Employee(EMP_ID = "9002")
        state = inspect(emp)
        print(state.transient)

        session.add(emp)
        state = inspect(emp)
        print(state.pending)

    def test_identity_set(self):
        emp1 = session.query(Employee).filter_by(EMP_ID='1001').first()
        emp2 = session.query(Employee).filter_by(EMP_ID='1002').first()

        info = session
        print(emp1 == emp2)


if __name__ == "__main__":
    unittest.main()


