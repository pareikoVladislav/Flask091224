# from pydantic import BaseModel
#
#
# class Address(BaseModel):
#     city: str
#     street: str
#     house_numb: int
#     index: int
#
#
# class User(BaseModel):
#     id: int
#     name: str
#     age: int
#     is_active: bool = True
#     address: Address
#
#
# address = Address(city="Minsk", street="Street", house_numb=13, index=6000)
# user = User(id=2, name="Tomas", age=27, address=address)
#
# print(user)
# print(user.address.street)


# ==============================================================
# import re
# from enum import StrEnum
# from pydantic import BaseModel
# from datetime import date
#
#
# class TestType(StrEnum):
#     BLOOD = "blood"
#     XRAY = "xray"
#     MRI = "mri"
#
#
# class LabTestBase(BaseModel):
#     patient_id: int
#     test_type: TestType
#     test_date: date
#
#
# class LabTestRequest(LabTestBase):
#     notes: str | None = None
#     # notes: Optional[str]
#
#
# class LabTestResponse(LabTestBase):
#     id: int
#     result: str | None = None
#     is_completed: bool
#
#     def is_urgent(self) -> bool:
#         if not self.result:
#             return False
#
#         if "гемоглобин" in self.result.lower():
#             match_patt = re.search(r"(\d+)\s*г/л", self.result.lower())
#
#             if match_patt:
#                 value = int(match_patt.group(1))
#                 return value < 80 or value > 150
#
#         return False
#
#
# request_data = {
#     "patient_id": 101,
#     "test_type": "blood",
#     "test_date": "2025-06-11",
#     "notes": "Анализ натощак"
# }
#
# response_data = {
#     "id": 5001,
#     "patient_id": 101,
#     "test_type": "blood",
#     "test_date": "2025-06-11",
#     "is_completed": True,
#     "result": "Гемоглобин: 50 г/л"
# }
#
# valid_request = LabTestRequest(**request_data)
# valid_response = LabTestResponse(**response_data)
#
# print(valid_request)
# print(valid_response)
#
# print({"urgent": valid_response.is_urgent()})



# from pydantic import BaseModel, Field
# from decimal import Decimal
#
#
# class Product(BaseModel):
#     name: str
#     description: str = Field(default=None, description="Описание товара") # -> ""
#     price: Decimal = Field(gt=0, max_digits=6, decimal_places=2) # 8888.88
#     in_stock: bool = Field(default=True, alias="available") # ... -> elipsys
#
#
# product = Product(
#     name="Chair",
#     price=Decimal("9.23"),
#     # available=False
# )
#
# print(product)
# print(product.description)
# print(product.in_stock)



from pydantic import (
    BaseModel, EmailStr,
    HttpUrl, Field,
    field_validator, ConfigDict,
    model_validator
)
from decimal import Decimal
import typing
from datetime import datetime

from pydantic_core.core_schema import DictSchema


class Product(BaseModel):
    name: str
    price: Decimal
    tags: list[str]


class User(BaseModel):
    full_name: str
    age: int
    email: EmailStr
    homepage: HttpUrl # https://
    # products: list[Product] = []  # WRONG!!!!
    products: list[Product] = Field(default_factory=list)
    created_at: datetime

# NEW VARIANT (pydantic v2)
    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda value: value.strftime("%d-%m-%Y %H:%M")
        }
    )

# OLD VARIANT (pydantic v1)
    # class Config:
    #     str_strip_whitespace = True
    #     validate_assignment = True # позволяет валидировать уже созданные объекты (обновление данных)
    #     json_encoders = {
    #         datetime: lambda value: value.strftime("%d-%m-%Y %H:%M")
    #     }

    @field_validator('email') # ...@example.com | gmail.com
    def validate_email(cls, value: str) -> str:
        # test.email@gmail.com + split("@") -> ['test.email', 'gmail.com'] + [-1] -> gmail.com
        allowed_domains = {'example.com', 'gmail.com'}
        email_domain = value.split("@")[-1]

        if email_domain not in allowed_domains:
            raise ValueError(f"Email must be from one of allowed domains: {', '.join(allowed_domains)}")

        return value


user = User(
    full_name="J. Johanson",
    age=32,
    email="j.johanson@gmail.com",
    homepage="https://example.com",
    created_at=datetime(year=2023, month=5, day=21, hour=15, minute=42)
)


print(user)

print(user.model_dump_json(indent=4))

# user.email = "j.johanson@mail.ru"
# print(user)

# def foo(data: list | None = None):
#     if not data:
#         data = []
#
#     ...


def process_user_input(data):
    ...