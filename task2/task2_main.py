from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import pandas as pd

db_connect = create_engine('sqlite:///stockdata.db',connect_args={'check_same_thread': False})
conn = db_connect.connect() #connect to the database 
app = Flask(__name__)
api = Api(app)

def create_top_gainer_df(df,df2): #the function generates the desired dataframe, by manipulating the two given dataframes 
    numbers = [i for i in range(1,21)]
    df["numbers"] = numbers
    df2["numbers"] = numbers
    df.set_index('numbers')
    df2.set_index('numbers')
    df['answer'] = df['4. close'] - df2['4. close']
    df['percentage_change'] = (df['answer']/df2['4. close'])*100
    df['rank'] = df['percentage_change'].rank(ascending=0)
    df = df.set_index('rank')
    df = df.sort_index()
    df3 = df[['Stock','percentage_change','numbers']].head(10).copy()
    df3 = df3.set_index('numbers')
    return df3

def create_top_losers_df(df,df2):
    numbers = [i for i in range(1,21)]
    df["numbers"] = numbers
    df2["numbers"] = numbers
    df.set_index('numbers')
    df2.set_index('numbers')
    df['answer'] = df['4. close'] - df2['4. close']
    df['percentage_change'] = (df['answer']/df2['4. close'])*100
    df['rank'] = df['percentage_change'].rank()
    df = df.set_index('rank')
    df = df.sort_index()
    df3 = df[['Stock','percentage_change','numbers']].head(10).copy()
    df3 = df3.set_index('numbers')
    return df3
  

class TopGainers(Resource):
    def get(self):
        df = pd.read_sql("""
                    SELECT *
                    FROM todays_stock_data
                    """, conn)
        df2 = pd.read_sql("""
                    SELECT *
                    FROM yesterdays_stock_data
                    """, conn)

        df3 = create_top_gainer_df(df,df2)
        result = df3.set_index('Stock').T.to_dict()
        result = dumps(result, indent=4, separators=(',', ': '))
        return result

class TopLosers(Resource):
    def get(self):
        df = pd.read_sql("""
                    SELECT *
                    FROM todays_stock_data
                    """, conn)
        df2 = pd.read_sql("""
                    SELECT *
                    FROM yesterdays_stock_data
                    """, conn)

        df3 = create_top_losers_df(df,df2)
        result = df3.set_index('Stock').T.to_dict()
        result = dumps(result, indent=4, separators=(',', ': '))
        return result  


class WeeklyReport(Resource):
    def get(self):
        df = pd.read_sql("""
                    SELECT *
                    FROM weekly_report
                    """, conn)
                    
        result = df.set_index('Stock').T.to_dict()
        result = dumps(result, indent=4, separators=(',', ': '))
        return result
        

api.add_resource(TopGainers, '/get_top_gainers') # Route_1
api.add_resource(TopLosers, '/get_top_losers') # Route_2
api.add_resource(WeeklyReport, '/generate_weekly_report') # Route_3


if __name__ == '__main__':
     app.run(port='5002')
     