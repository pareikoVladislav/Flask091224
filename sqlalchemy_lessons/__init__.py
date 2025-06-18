__all__ = (
    'engine',
    'Base'
)

from pathlib import Path

from pydantic import BaseModel
from pydantic_core.core_schema import nullable_schema
from sqlalchemy import create_engine, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.testing.schema import mapped_column

proj_path = Path(__file__).parent.parent

engine = create_engine(
    url=f"sqlite:///{proj_path}/database.db"
)

Base = declarative_base()


# class User(Base):
#     __tablename__ = "user"
#     id: int = mapped_column(Integer, primary_key=True)
#     name: str = mapped_column(String(20))
#     age: int = mapped_column(Integer, nullable=True)
#
#
# class UserCreateSchema(BaseModel):
#     name: str
#     age: int | None = None
#
#     model_config = {
#         "from_attributes": True
#     }
#
#
# user_input_data = { # Raw data
#     "name": "Alice",
#     "age": 34
# }
#
# validated_data = UserCreateSchema.model_validate(user_input_data).model_dump()
#
# user = User(**validated_data)
#
# session.add(user)
# session.commit()
# session.close()
