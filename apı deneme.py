import os
import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()
APP_ID = os.getenv("my_api")


rsp = requests.get(f"https://openexchangerates.org/api/latest.json?app_id={APP_ID}").json()

#pandas 

df = pd.DataFrame(rsp['rates'].items(), columns=['currency_name', 'currency_rate'])

#add new colums for currency date

df['currency_date'] = datetime.fromtimestamp(rsp['timestamp'])

print(df)



