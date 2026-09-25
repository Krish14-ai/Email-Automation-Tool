from pydantic import BaseModel, field_validator, Field, EmailStr, ValidationInfo
from typing import Annotated


class Mails(BaseModel):

    name: Annotated[
        str,
        Field(
            ...,
            description="Please enter your name",
            min_length=2,
            max_length=100
        )
    ]

    user_id: Annotated[
        str,
        Field(
            ...,
            pattern=r"^\d{3}$",
            description="User Id must be of 3 digits"
        )
    ]

    mail: Annotated[
        EmailStr,
        Field(
            ...,
            description="Please enter your email"
        )
    ]

    @field_validator("mail", mode="after")
    @classmethod
    def validate_mail(cls, data, info: ValidationInfo):

        user_id = info.data.get("user_id")

        if "-" in str(data):
            raise ValueError(
                f"Invalid Gmail found at user {user_id}"
            )

        return data
    
    