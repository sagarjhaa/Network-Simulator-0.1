__author__ = 'sjha1'


import pymongo

conn = pymongo.MongoClient("localhost",27017)

db = conn['school']
coll = db['students']
doc = coll.find({})


for eachdoc in doc:
    for key,value in eachdoc.items():

        #coll.up

        if key == "scores":
            scores = value
            i = 2
            j = 3
            if scores[i]["score"] < scores[j]["score"]:
                #print scores[i]["score"],scores[j]["score"]
                scores.pop(i)
            else:
                scores.pop(j)
            print scores

        #print eachdoc[key],value
