import pandas as pd
import time
from alpha_vantage.timeseries import TimeSeries
from sqlalchemy import create_engine

API_key = 'G24DSVXPY2GVBJ3M'
count = 0
df = pd.DataFrame()
frames = []

def get_data(data):
    frames.append(data)

ts = TimeSeries(API_key, output_format='pandas')
with open("ticker_symbols.txt","r") as f:
    tickers= [(ticker.strip()).split() for ticker in f]

for ticker in tickers:
    data, meta = ts.get_daily(ticker)
    df_new = pd.DataFrame
    dict = {"weekly_avg" : data['4. close'].head(7).mean(),
            "weekly_max" : data['4. close'].head(7).max(),
            "weekly_min" : data['4. close'].head(7).min(),
            "ticker" : ticker}
    df_new = pd.DataFrame(dict, index=[count])
    print(df_new)
    get_data(df_new)
    count += 1
    if count%5 == 0 and count != 20: #alpha vantage limits our calls to 5 per minute, so we need to add a delay 
        time.sleep(60)

df = pd.concat(frames) 
df.insert(loc = 0,column='Stock',value=tickers)
print(df)
df.to_csv(r'C:\Users\rajag\Desktop\stock_weekly_report.csv') #storing the file in a local directory 
