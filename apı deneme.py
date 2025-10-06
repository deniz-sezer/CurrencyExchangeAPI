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
# API'den alınan döviz kurları pandas DataFrame'e aktarılır ve veri zaman bilgisi eklenir.
# Kullanıcı 'currency_name' değişkenine istediği para birimini (örneğin "USD", "EUR", "TRY" vb.) girerek o birime ait kuru görüntüleyebilir.
#currency_name = "TRY"
#filtered_df = df[df['currency_name']==currency_name]
#print(filtered_df)







