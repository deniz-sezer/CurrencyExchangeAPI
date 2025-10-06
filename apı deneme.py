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

# Exchange rate data from the API is loaded into a pandas DataFrame, with the timestamp converted to datetime.
# Users can enter any currency code in 'currency_name' (e.g., "USD", "EUR", "TRY") to display that currency's rate.
#example
#currency_name = "TRY"
#filtered_df = df[df['currency_name']==currency_name]
#print(filtered_df)







