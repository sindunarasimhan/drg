from pymongo import MongoClient
import collections
from collections import Counter
connection = MongoClient('z')
import json
import re

db = connection.sydneysiege
hashes = []
hashdict = collections.defaultdict(int)
for cursor in db.tweets.find({"hashtags":{"$exists":True},"$where":"this.hashtags.length>=1"}):
    hashlist = cursor['hashtags']
    for s in hashlist:
            s = s.encode("utf-8")
            hashes.append(s)

c = Counter(hashes)
lim = raw_input("Enter hashtags you want to see:")
limit = int(lim)
orderedlist = c.most_common(limit)
for item in orderedlist:
    print item[0],item[1]