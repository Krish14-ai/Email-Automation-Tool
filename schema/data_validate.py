import pandas as pd 
import pydantic
from pydantic import BaseModel


def get_all_mails():
    data = pd.read_csv(r"C:\Users\Krish\Downloads\Email-Automation-Tool\mails\data\recipients.csv")
    
    return data["mail"].tolist()

