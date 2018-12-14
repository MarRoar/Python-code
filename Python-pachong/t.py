import pymongo

client = pymongo.MongoClient('localhost', 27017)

db = client.mar

# collection is stu
# stu = db.stu

# s1 = {'name': 'aa', 'gender': 2}
# s1_id = stu.insert_one(s1).inserted_id


list1 = db.list1
s2 = list1.find()

for cur in list1.find():
	print cur


