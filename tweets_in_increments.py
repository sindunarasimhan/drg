#TODO:Console Input of DB and Limits. Write output to CSV with timestamp
#Tweet viz analysis script to visualize tweet counts for an applied code
from pymongo import MongoClient
import collections
import datetime

connection = MongoClient('z')
db = connection.sydneysiege
timestamplist = []
dateStart_str = "2014-12-15 00:00:00"
dateEnd_str =  "2014-12-17 11:59:59"
dateStart = datetime.datetime.strptime(dateStart_str, "%Y-%m-%d %H:%M:%S")
dateEnd = datetime.datetime.strptime(dateEnd_str, "%Y-%m-%d %H:%M:%S")
count = 0
while dateStart < dateEnd:
    startime = dateStart
    endtime = dateStart+datetime.timedelta(minutes=10)
    dateStart = endtime
    #print startime
    print db.lakemba.find({"codes.second_code":"Uncertainty","created_ts":{"$gte":startime,"$lt":endtime}}).count()