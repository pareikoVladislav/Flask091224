from pathlib import Path

from sqlalchemy import Table, Column, Integer, String, Text, create_engine
from sqlalchemy.orm import registry

Register = registry()

proj_path = Path(__file__).parent.parent
sqlite_engine = create_engine(
    url=f"sqlite:///{proj_path}/database.db"
)


# Classic Imperative style
news_table = Table(
    'news', Register.metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(120)),
    Column('description', Text)
)


class News:
    def __init__(self, title, description):
        self.title = title
        self.description = description


Register.map_imperatively(News, news_table)
Register.metadata.create_all(bind=sqlite_engine)
