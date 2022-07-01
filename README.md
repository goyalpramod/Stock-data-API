# dayzero-python-problem-my_submission

## How to setup
* import the libraries from requirements.txt <br />
It can be done by writing the following comand in the terminal <br />
```pip install -r requirements.txt```


### Task 1
<!-- one should have the configurations of postgreSQL with them.  -->
* One should avail their free API from alpha vantage. Using which one should update the API_key. <br />
* After updating the information in the code present in task1.py.
One can simply run it, it would store the information in the present directory as a .db file. <br />
* Alternatively if one has the credentials to his postgreSQL server you can directly store it there by running the following code.<br />
```engine = create_engine('postgresql://username:password@localhost:5432/name_of_database')```

### Task 2
* The location of the data should be present with the user. 
* After updating the information in db_connect one can start the server by simply running it.
* Then one can make requests to the api using the tests provided and observe the results.

## Approach

### Task 1
* We retrieve the stock_data of the desired ticker.
* A UUID was generated and the stock name were added to the data retrieved. 
* We take the top row as that represents latest data. 
* We append this to a list.
* **A delay of one minute has been added after 5 calls, because alpha vantage limits to 5 calls per minute.**
* Then after getting all the required data, we convert that into a pandas dataframe.
* Then we store it in a database.
* The given script has been scheduled to run daily at 10:30 that can be changed to the user's desired time.

### Task 2
* A connection to the database was established.
* Two functions ```create_top_gainers_df``` and ```create_top_losers_df``` were created. which would return to us our desired output. 
* Three routes were made for the api 
* TopGainers returns to us the top 10 stocks which had the biggest positive change in an ordered manner.
* TopLosers returns to us the top 10 stocks which had the biggest negative change in an ordered manner.
* WeeklyReport returns to us the weekly report of the stocks. Due to the ambiguity of the presence or absence of the data in the database an additional 
.py file has been provided. Namesly ```generating_weekly_report.py``` which would return to us the weekly report in the desired format.

## Result

### Task 1
* Result.csv has been provided to get a quick look at the output.
![task1_result](https://github.com/goyalpramod/dayzero-python-problem-my_submission/blob/main/images/task1_result.png)

### Task 2
* Results have been provided in the json format to get a quick glance. 
* Result of get_top_gainers <br />
![get_top_gainers_result](https://github.com/goyalpramod/dayzero-python-problem-my_submission/blob/main/images/get_top_gainers_result.png)
* Result of get_top_losers <br />
![get_top_losers_result](https://github.com/goyalpramod/dayzero-python-problem-my_submission/blob/main/images/get_top_losers_result.png)
* Result of weekly_report <br />
![weekly_report_result](https://github.com/goyalpramod/dayzero-python-problem-my_submission/blob/main/images/weekly_report_result.png)


## Problems encountered

### Task 1
* Alpha vantage limits to using 5 calls per minute, so one had to add a delay of 1 minute. 
* Calling the get_daily function in alpha vantage gives daily data of 20+ years, We do not require so much information. We just need the current information.
This is a waste of resources. 
* Complete name of the stocks were not present. So one had to hardcode them.

### Task 2
* Instead of using create_top_gainers_df and create_top_losers_df, Directly quering them could have been done. But due to the inability to produce optimal results 
one had to resort to making these functions.
* One has directly displayed weekly_report and no data manipulation has been done. This is due to the ambiguity of how one would recieve the data. But one has provided 
```generating_weekly_report.py``` which resolves the ambiguity and provides a means of getting the data exactly as we want it.

## Improvements

### Task 1 
* We can look into different ways to bypass the 5 calls per minute limit. Various other APIs were tried but alpha vantage came out at top. Buying the premium can be one possible solution.
* The schedule task would rewrite the present database every day that it runs. So we can make unique identifiers of each .db file and store them. 


### Task 2
* A basic front end can be developed. 
* Removal of redundant functions and instead using a query.
* Adding a user authorization.

<br />
<br />
<footer> Thank you, for giving your valuable time to review my submission. </footer>
