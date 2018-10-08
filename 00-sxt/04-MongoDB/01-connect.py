'''
1、MongoDB 的安装
2、pip install PyMongo 安装这个site插件
3、连接pycharm

https://juejin.im/post/5addbd0e518825671f2f62ee

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

# result = collection.insert(student)
# print(result)

student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}


result = collection.insert_many([student1, student2])
print(result)