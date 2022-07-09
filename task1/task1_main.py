import pandas as pd
import time
import schedule
from alpha_vantage.timeseries import TimeSeries
from sqlalchemy import create_engine
import uuid


def job():
    API_key = "G24DSVXPY2GVBJ3M"  # API key can be obtained from alpha vantage
    df = pd.DataFrame()
    frames = []
    stock_name = [
        "Tesla Inc",
        "Apple Inc",
        "Amazon.com, Inc.",
        "Microsoft Corporation",
        "META",
        "Google",
        "Nvidia",
        "NIO",
        "AMD",
        "Alphabet Inc Class C",
        "MasterCard Inc.",
        "Alibaba Group Holding Ltd - ADR",
        "Pfizer Inc.",
        "Coca-Cola Co",
        "Shopify Inc",
        "Mastercard Inc",
        "PepsiCo, Inc.",
        "Toyota Motor Corp",
        "A2Z Smart Technologies Corp",
        "Oracle",
    ]

    def get_data(data):
        frames.append(data)

    try:
        ts = TimeSeries(
            API_key, output_format="pandas"
        )  # Connects us to the alpha vantage API
    except:
        print("Unable to connect to alpha vantage")

    with open("ticker_symbols.txt", "r") as f:
        tickers = [(ticker.strip()).split() for ticker in f]

    for count, ticker in enumerate(tickers):
        try:
            data, meta = ts.get_daily(ticker)  # Retrieves the daily data from the API
        except:
            print("No data found for {t}".format(t=ticker))

        print(ticker)
        UUID = uuid.uuid1()
        data.insert(0, "ID", UUID)
        data.insert(1, "Stock Name", stock_name[count])
        print(data.head(1))
        get_data(data.head(1))
        count += 1
        if (
            count % 5 == 0 and count != 20
        ):  # alpha vantage limits our calls to 5 per minute, so we need to add a delay
            time.sleep(60)

    df = pd.concat(frames)
    df = df.iloc[:, :-1]  # drop last column
    df.insert(loc=0, column="Stock", value=tickers)

    # engine = create_engine('postgresql://postgres:admin@localhost:5432/stockdata')
    engine = create_engine(
        "sqlite:///stockdata.db", echo=True
    )  # creates a db file in the same directory
    df.to_sql("stock_data_new", engine)


while True:
    schedule.every().day.at("10:30:00").do(
        job
    )  # schedules a job that runs daily at 10:30 AM
