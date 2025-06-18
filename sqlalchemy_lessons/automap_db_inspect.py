from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import Mapped, declarative_base, mapped_column
from sqlalchemy.orm.base import Mapped

Base = declarative_base()


class News(Base):
    __tablename__ = 'news'

    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String(120))
    description = mapped_column(Text)


class Users(Base):
    __tablename__ = 'users'

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(25))
    age = mapped_column(Integer)
