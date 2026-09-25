import pydantic
from fastapi import FastAPI
from schema import data_validate 

app = FastAPI()

@app.get("/")
def enter():
    return {"message" : "hello"}

@app.get("/mails")
def get_mails():
    mails = get_all_mails()
    
    return {"all mails" : mails}
