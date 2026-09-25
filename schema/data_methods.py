import pandas as pd 

def get_all_mails():
    data = pd.read_csv(r"C:\Users\Krish\Downloads\Email-Automation-Tool\mails\data\recipients.csv")
    
    return data["mail"]
