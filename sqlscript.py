import mysql.connector
import sys
import dateutil.parser
from random import randint
connection = mysql.connector.connect(host = '127.0.0.1',user = 'root', password = '',db='Ebola1')
cursor = connection.cursor()
cursor.execute ("select text FROM tweet3 LIMIT 10000")
tweets = []
data = cursor.fetchall()
for row in data:
    tweets.append(row)
count = 0
while count < 1000:
    print tweets[randint(0,10000)]
    count = count+1
cursor.close()
connection.close()
sys.exit()