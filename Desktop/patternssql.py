import MySQLdb
import collections
import MySQLdb.cursors as cursors
import sys
import re
from itertools import islice
from collections import Counter
connection = MySQLdb.connect(host = '127.0.0.1',user = 'root',db='Ebola1',cursorclass = cursors.SSCursor)
cursor = connection.cursor()
cursor.execute ("select text FROM tweet3 WHERE text LIKE '%#%'")
tweets = []
data = cursor.fetchall()
hashtags = [];
hashdict = collections.defaultdict(int)
pat = re.compile(r'\B#\w+')
for row in data:
    s = str(row)
    s = s.lower()
    hash = pat.findall(s)
    if len(hash) > 0:
        hashtags.append(hash)
for list in hashtags:
    for val in list:
        if val in hashdict:
            hashdict[val]+=1
        else:
            hashdict[val] = 1
            
c=Counter(hashdict)
orderedlist = c.most_common()
print("Hashtags are available to be viewed in as list")
print("The list is ordered from most used to least used")
var = raw_input("Enter the top number of #hashtags you'd like to see: ")
num = 0
limit = int(var)
for item in islice(orderedlist,0,limit):
    print item
cursor.close()
connection.close()
sys.exit()