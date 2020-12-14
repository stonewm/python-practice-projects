from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"

    emp_id = Column("EMP_ID", String(255), primary_key=True)
    first_name = Column("FIRST_NAME", String(255))
    last_name = Column("LAST_NAME", String(255))
    gender = Column("GENDER", String(255))
    age = Column("AGE", Integer)
    email = Column("EMAIL", String(255))
    phone = Column("PHONE_NR", String(255))
    education = Column("EDUCATION", String(255))
    marital_stat = Column("MARITAL_STAT", String(255))
    children = Column("NR_OF_CHILDREN", Integer)

    def __repr__(self):
        return "Employee <{emp_id},{first_name},{last_name},{gender},{age},{email},{phone},{education},{marital_stat},{children}>".format(
            emp_id=self.emp_id,
            first_name=self.first_name,
            last_name=self.last_name,
            gender=self.gender,
            age=self.age,
            email=self.email,
            phone=self.phone,
            education=self.education,
            marital_stat=self.marital_stat,
            children=self.children
        )