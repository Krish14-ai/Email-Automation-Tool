import pandas as pd 
from pydantic import BaseModel, field_validator, Field
from typing import Annotated

class mails(BaseModel):
    name = Annotated[str, Field(..., description= "please Enter your name", min_length= 2, max_length=100)]
    
    
