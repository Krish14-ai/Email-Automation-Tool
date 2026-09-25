import pandas as pd 
from pydantic import BaseModel, field_validator, Field, EmailStr
from typing import Annotated

class mails(BaseModel):
    name = Annotated[str, Field(..., description= "please Enter your name", min_length= 2, max_length=100)]
    
    user_id = Annotated[int, Field(..., ge= 0,description= "please enter your user id",min_length= 1)]

    mail = Annotated[EmailStr, Field(..., description= "Please enter your gmail")]
    
    
    @field_validator("mail", mode = "after")
    def validate_mail(cls, data):
        
        for i, row in enumerate(data.itertuples(index=False), start=1):
            user_id = row.user_id
            email = row.mail
            if "-" in email : 
                raise ValueError(f"invalid gamil found at user {user_id}")            