# Week 2 CRUD Homework 2.2
# In the shell, we first import the data file grades.json to the db students, and name the new collection 'grades'
# mongoimport --drop -d students -c grades grades.json
# the new collection should have 800 documents 
# check in mongo shell: use students
#                       db.grades.count() 
# sample documents: 
# { "_id" : ObjectId("50906d7fa3c412bb040eb579"), "student_id" : 0, "type" : "homework", "score" : 14.8504576811645 }
# { "_id" : ObjectId("50906d7fa3c412bb040eb578"), "student_id" : 0, "type" : "quiz", "score" : 31.95004496742112 }
# our goal is to drop the lowest homework score for each student

import pymongo

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.students
grades = db.grades

def find():
    try:
        for i in range(0, 200):
            remove_id_array = grades.find({'student_id': i, "type":"homework"}).sort('score', pymongo.ASCENDING).limit(1)
            for id_to_be_removed in remove_id_array:
                grades.remove({'_id': id_to_be_removed['_id']})
    except Exception as e:
        print "Unexpected error:", type(e), e
        
    print grades.count()

if __name__ == '__main__':
    find()
