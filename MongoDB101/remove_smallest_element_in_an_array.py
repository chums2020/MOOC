# remove the lowest homework score for each student.
# Since there is a single document for each student containing an array of scores,
# you will need to update the scores array and remove the homework.

# example document:
# {
#         "_id" : 137,
#         "name" : "Tamika Schildgen",
#         "scores" : [
#                 {
#                         "type" : "exam",
#                         "score" : 4.433956226109692
#                 },
#                 {
#                         "type" : "quiz",
#                         "score" : 65.50313785402548
#                 },
#                 {
#                         "type" : "homework",
#                         "score" : 89.5950384993947
#                 },
#                 {
#                         "type" : "homework",
#                         "score" : 54.75994689226145
#                 }
#         ]
# }
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.school
students = db.students

for i in range(0, 200):
    cursor = students.find_one({'_id': i})
    score1 = cursor['scores'][2]['score']
    score2 = cursor['scores'][3]['score']
    if score1 > score2:
        students.update({'_id': i}, {'$pull': {'scores':{'type':'homework','score':score2}}})
    else:
        students.update({'_id': i}, {'$pull': {'scores':{'type':'homework','score':score1}}})
