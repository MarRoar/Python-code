'''
MongoDB 查找
插入数据后，我们可以利用find_one()或find()方法进行查询，
其中find_one()查询得到的是单个结果，
find()则返回一个生成器对象。示例如下：
'''

import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test

#
collection = db.students
# student = {
#     'id': '202181008',
#     'name': 'LP',
#     'age': 25,
#     'gender': 'male'
# }
#
# student1 = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
# student2 = {
#     'id': '20170202',
#     'name': 'Mike',
#     'age': 21,
#     'gender': 'male'
# }

print("find_one----------------")
result1 = collection.find_one({'name': 'LP'})
print(type(result1))
print(result1)

print("find----------------")
# 返回结果是Cursor类型，它相当于一个生成器，我们需要遍历取到所有的结果，其中每个结果都是字典类型。
result2 = collection.find({'age': 20})
print(type(result2))
print(result2)

