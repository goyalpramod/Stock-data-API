import pandas as pd
import time
import schedule
from alpha_vantage.timeseries import TimeSeries
from sqlalchemy import create_engine
import uuid

def job():
    API_key = 'G24DSVXPY2GVBJ3M' #API key can be obtained from alpha vantage
    count = 0
    df = pd.DataFrame()
    frames = []
    stock_name = ["Tesla Inc", "Apple Inc", "Amazon.com, Inc.", "Microsoft Corporation", "META", "Google", "Nvidia"
    , "NIO", "AMD", "Alphabet Inc Class C", "MasterCard Inc.", "Alibaba Group Holding Ltd - ADR", "Pfizer Inc.",
    "Coca-Cola Co","Shopify Inc", "Mastercard Inc", "PepsiCo, Inc.", "Toyota Motor Corp", "A2Z Smart Technologies Corp","Oracle"]


    def get_data(data):
        frames.append(data)

    ts = TimeSeries(API_key, output_format='pandas') #retrieve the data from alpha vantage
    with open("ticker_symbols.txt","r") as f:
        tickers= [(ticker.strip()).split() for ticker in f]

    for ticker in tickers:
        data, meta = ts.get_daily(ticker)
        print(ticker)
        UUID = uuid.uuid1()
        data.insert(0,'ID', UUID)
        data.insert(1, 'Stock Name', stock_name[count])
        print(data.head(1))
        get_data(data.head(1))
        count += 1
        if count%5 == 0 and count != 20: #alpha vantage limits our calls to 5 per minute, so we need to add a delay 
            time.sleep(60)

    df = pd.concat(frames)
    df = df.iloc[:, :-1] # drop last column 
    df.insert(loc = 0,column='Stock',value=tickers)

    
    engine = create_engine('sqlite:///stockdata.db', echo=True) #creates a db file in the same directory
    df.to_sql('stock_data_new', engine)

schedule.every().day.at("10:30:00").do(job) #schedules a job that runs daily at 10:30 AM

