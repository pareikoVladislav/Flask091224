from pydantic import BaseModel, EmailStr, Field, AliasChoices, field_validator, model_validator
from datetime import datetime


class Vehicle(BaseModel):
    engine_type: str
    doors: int
    radio: bool


class VehicleRequest(Vehicle):
    ...


class VehicleResponse(Vehicle):
    id: int
    response_date: datetime


class User(BaseModel):
    name: str
    surname: str = Field(pattern=r"^[A-Z]+$")
    age: int = Field()
    vehicle: Vehicle
    # phones: list[str] = [] # WRONG!!!
    phones: list[str] = Field(default_factory=list) # OK

    @field_validator('name', 'surname')
    def validate_and_normalize_fields(cls, value):
        # validate
        # normalize
        ...

    # @model_validator(mode='after')
    # def validate_data(cls, model):
    #     model.age

    @model_validator(mode='before')
    def validate_data(cls, attrs):
        attrs['age']


vehicle = Vehicle(...)

user = User(..., vehicle=vehicle)

json_data = """{
    "name": "",
    "surname": "",
    "age": 28,
    "vehicle": {
        ...
    }
}"""
