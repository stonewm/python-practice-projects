from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Address
import unittest

engine = create_engine("sqlite:///testdb.db", echo=False)
session = sessionmaker(bind=engine)()

class TestRelation(unittest.TestCase):
    def test_query_via_join(self):
        result = session.query(User, Address).join(Address).all()
        print(result)
        for item in result:
            print(item[0].id, item[0].fullname, item[1].email_address)

    def test_query_via_relation(self):
        result = session.query(User).all()
        for item in result:
            addresses = item.addresses
            for addr in addresses:
                print(item.id, item.fullname, addr.email_address)

    def test_query_from_child(self):
        result = session.query(Address).all()
        for addr in result:
            print(addr.id, addr.email_address, addr.user.fullname)


    def test_query_multiple_tables(self):
        """
        这种方式相当于笛卡尔乘积
        """
        result = session.query(User, Address).all()
        print(type(result))
        for item in result:
            print(item)

    def test_query_from_parent(self):
        user = session.query(User).filter_by(id=2).first()
        addresses = user.addresses
        for item in addresses:
            print(item)

    def test_get_address_manually(self):
        """
        不管数据库是否建立关系，sqlalchemy是否建立关系
        都可以用下面手工的方式查询和获取
        :return:
        """
        user = session.query(User).filter_by(id=2).first()
        addresses = session.query(Address).filter(Address.user_id == user.id).all()
        print(addresses)

    def test_create_user_and_addr(self):
        """
        手工的方式，没有利用SA的relationship
        """
        user = User(id=3, name="Alice", fullname="Alice Brown")
        addr = Address(id=4, email_address="alice@smarter.com", user_id=3)
        session.add(user)
        session.add(addr)
        session.commit()

    def test_create_user_and_addr2(self):
        user = User(id=3, name="Alice", fullname="Alice Brown")
        user.addresses = [
            Address(id=4, email_address="alice@smarter.com"),
            Address(id=5, email_address="alice@smarter.com")
        ]
        session.add(user)
        session.commit()


    def test_create_user_and_addr3(self):
        alice = User(id=3, name="Alice", fullname="Alice Brown")
        addr = Address(id=4, email_address="alice@smarter.com", user=alice)
        session.add(alice)
        session.add(addr)
        session.commit()


    def test_delete_user_and_addr(self):
        """
        维护参照完整性，或者SQLAlchemy维护了级联删除
        """
        user = session.query(User).filter_by(id=3).first()
        session.delete(user)
        session.commit()


if __name__ == "__main__":
    unittest.main()

