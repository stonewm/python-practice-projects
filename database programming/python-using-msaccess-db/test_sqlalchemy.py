import unittest
from employee_sqlalchemy.models import Employee
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker


engine = create_engine("access+pyodbc://EMP_MSACCESS")
Session = sessionmaker(bind=engine)
session = Session()

class TestSqlalchemy(unittest.TestCase):

    def test_query(self):
        employees = session.query(Employee).all()
        for emp in employees:
            print(emp)

    def test_query_one(self):
        employees = session.query(Employee).filter(Employee.first_name=="Ted").all()
        for emp in employees:
            print(emp)

    def test_insert(self):
        new_emp = Employee(
            emp_id =9001,
            first_name = "Alice",
            last_name = "Brown"
        )
        session.add(new_emp)
        session.commit()
        session.close()

    def test_update(self):
        emp = session.query(Employee).get(9001)
        if emp is not None:
            emp.age = 20
            session.commit()
            session.close()

    def test_delete(self):
         emp = session.query(Employee).get(9001)
         if emp is not None:
            session.delete(emp)
            session.commit()
            session.close()


if __name__ == "__main__":
    unittest.main()