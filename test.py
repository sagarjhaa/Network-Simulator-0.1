#__author__ : Sjha1

import pymongo


connection = pymongo.MongoClient("mongodb://localhost")

db = connection.students
collection = db.grades

query = {"type":"exam"}

document = collection.find(query)


#for i in o:
    #print i[u'student_id'],i[u'score']
