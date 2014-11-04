import MySQLdb
import collections
import MySQLdb.cursors as cursors
import sys
import re
from itertools import islice
from collections import Counter
connection = MySQLdb.connect(host = '127.0.0.1',user = 'root',db='Ebola1',cursorclass = cursors.SSCursor)
cursor = connection.cursor()
cursor.execute ("select text FROM tweet3 WHERE text LIKE '%@%'")
tweets = []
data = cursor.fetchall()
usernames = [];
userdict = collections.defaultdict(int)
pat = re.compile(r'\B@\w+')
for row in data:
    s = str(row)
    s = s.lower()
    name = pat.findall(s)
    if len(name) > 0:
        usernames.append(name)
for list in usernames:
    for val in list:
        if val in userdict:
            userdict[val]+=1
        else:
            userdict[val] = 1
            
c=Counter(userdict)
orderedlist = c.most_common()
print("@username mentions are available to be viewed in as list")
print("The list is ordered from most used to least used")
var = raw_input("Enter the top number of @username you'd like to see: ")
print("List of (@usermentions,numberoftimes they occur)")
num = 0
limit = int(var)
for item in islice(orderedlist,0,limit):
    print item
cursor.close()
connection.close()
sys.exit()