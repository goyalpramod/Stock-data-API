# dayzero-python-problem-my_submission

How to setup->
import the libraries from requirements.txt 
(provide code snipped on how to do so too)
pip install -r requirements.txt
For task 1, one should have the configurations of postgreSQL with them. 
And one should avail their free API from alpha vantage.

After updating the information in the code present in task1.py
One can simply run it and then see the data in postgreSQL
(Code snippet for query)

For task 2,

Approach.

task 1,
retrieve the data from alpha vantage 5 at a time 
take the top row 
append it in a list 
convert the list into a dataframe 
connect to postgreSQL and store the data in the database 
schedule it to run everyday at the specified time 

task 2,


Issues

task 1, 
alpha vantage limits to using 5 calls per minute 
everyone may not have postgreSQL 

task 2,
assumption that weekly report will be the way we want it to be. 

Improvements

task 1, 
we can look into different ways to bypass the 5 calls per minute limit 
we can directly store it as a database in the same directory 

task 2,
