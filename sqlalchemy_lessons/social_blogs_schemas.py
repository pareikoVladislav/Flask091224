from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, model_validator, ValidationError


class UserCreateSchema(BaseModel):
    first_name: str = Field(..., max_length=25)
    last_name: str | None = Field(default=None, max_length=30)
    email: EmailStr
    password: str
    repeat_password: str
    phone: str | None = Field(default=None, max_length=45)
    role_id: int

    model_config = {
        "from_attributes": True
    }

    @model_validator(mode='after')
    def validate_passwords(cls, model):
        if model.password != model.repeat_password:
            raise ValidationError("Passwords do not match.")

        return model


class UserUpdateSchema(BaseModel):
    first_name: str | None = Field(default=None, max_length=25)
    last_name: str | None = Field(default=None, max_length=30)
    email: EmailStr | None = None
    phone: str | None = Field(default=None, max_length=45)
    role_id: int | None = None
    rating: float | None = None
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "from_attributes": True
    }


class RoleMiniSchema(BaseModel):
    id: int
    name: str

    model_config = {
        "from_attributes": True
    }


class UserResponseSchema(BaseModel):
    id: int
    first_name: str
    last_name: str | None
    email: str
    phone: str | None
    rating: float
    role: RoleMiniSchema | None
    deleted: bool
    created_at: datetime
    updated_at: datetime | None
    deleted_at: datetime | None

    model_config = {
        "from_attributes": True
    }


class NewsForUserSchema(BaseModel):
    id: int
    title: str
    moderated: bool
    created_at: datetime

    model_config = {
        "from_attributes": True
    }


class UserWithNewsSchema(BaseModel):
    id: int
    first_name: str
    last_name: str | None
    email: str
    phone: str | None
    role_id: int
    deleted: int
    news: list[NewsForUserSchema]

    model_config = {
        "from_attributes": True
    }

