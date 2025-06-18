import logging

from pathlib import Path
from sqlalchemy import create_engine, Column, Integer, String, insert, Table, Text
from sqlalchemy.orm import sessionmaker, declarative_base, registry


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('sqlalchemy.engine')
logger.setLevel(logging.INFO)


# engine = create_engine(
#     url="mysql+pymysql://ich1:ich1_password_ilovedbs@ich-edit.edu.itcareerhub.de:3306/alchemy_lesson"
# )
#
#
# print(engine)


proj_path = Path(__file__).parent.parent
Base = declarative_base()


sqlite_engine = create_engine(
    url=f"sqlite:///{proj_path}/database.db"
)

print(sqlite_engine)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    age = Column(Integer)

Session = sessionmaker(bind=sqlite_engine)
session = Session()


print(session)

Base.metadata.create_all(bind=sqlite_engine)

user = User(
    name="Ivan",
    age=29
)

session.add(user)

session.commit()
session.close()


# user = User(...) # Transient
#
# session.add(user) # Pending
#
# session.commit() # Persistent
#
# session.close() # Detached v1
# session.expunge() # Detached v2 (объект отвязан от сессии, сессия открыта)
#
#
# user = User.query.get(id=1)
# user.delete()
# session.commit() # Deleted
# session.close()


# print(range(1, 5))
# test_list = []
#
# for i in range(1, 5):
#     test_list.append(i)
#
# print(test_list)
