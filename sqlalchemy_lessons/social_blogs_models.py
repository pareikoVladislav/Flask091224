from typing import List, Optional

from sqlalchemy import Float, ForeignKeyConstraint, Index, Integer, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship

Base = declarative_base()


class Role(Base):
    __tablename__ = 'role'

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(20), nullable=False)

    users: Mapped[List['User']] = relationship('User', uselist=True, back_populates='role')


class User(Base):
    __tablename__ = 'user'
    __table_args__ = (
        ForeignKeyConstraint(['role_id'], ['role.id'], name='user_ibfk_1'),
        Index('email', 'email', unique=True),
        Index('role_id', 'role_id')
    )

    id = mapped_column(Integer, primary_key=True)
    first_name = mapped_column(String(25), nullable=False)
    email = mapped_column(String(75), nullable=False)
    password = mapped_column(String(255), nullable=False)
    repeat_password = mapped_column(String(255), nullable=False)
    last_name = mapped_column(String(30))
    phone = mapped_column(String(45))
    role_id = mapped_column(Integer)
    rating = mapped_column(Float, server_default=text("'0'"))
    deleted = mapped_column(TINYINT(1), server_default=text("'0'"))
    created_at = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = mapped_column(TIMESTAMP)
    deleted_at = mapped_column(TIMESTAMP)

    role: Mapped[Optional['Role']] = relationship('Role', back_populates='users')
    news: Mapped[List['News']] = relationship('News', uselist=True, back_populates='author')
    comments: Mapped[List['Comment']] = relationship('Comment', uselist=True, back_populates='author')


class News(Base):
    __tablename__ = 'news'
    __table_args__ = (
        ForeignKeyConstraint(['author_id'], ['user.id'], name='news_ibfk_1'),
        Index('author_id', 'author_id')
    )

    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String(100), nullable=False)
    content = mapped_column(Text, nullable=False)
    author_id = mapped_column(Integer)
    moderated = mapped_column(TINYINT(1), server_default=text("'0'"))
    created_at = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = mapped_column(TIMESTAMP)

    author: Mapped[Optional['User']] = relationship('User', back_populates='news')
    comments: Mapped[List['Comment']] = relationship('Comment', uselist=True, back_populates='news')


class Comment(Base):
    __tablename__ = 'comment'
    __table_args__ = (
        ForeignKeyConstraint(['author_id'], ['user.id'], name='comment_ibfk_1'),
        ForeignKeyConstraint(['news_id'], ['news.id'], name='comment_ibfk_2'),
        Index('author_id', 'author_id'),
        Index('news_id', 'news_id')
    )

    id = mapped_column(Integer, primary_key=True)
    content = mapped_column(Text, nullable=False)
    author_id = mapped_column(Integer)
    news_id = mapped_column(Integer)
    created_at = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = mapped_column(TIMESTAMP)

    author: Mapped[Optional['User']] = relationship('User', back_populates='comments')
    news: Mapped[Optional['News']] = relationship('News', back_populates='comments')
