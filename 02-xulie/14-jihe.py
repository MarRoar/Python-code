
'''
    集合
        集合底层是用字典来实现的，但是只有字典的键，

    使用 set() 将列表，元组等可迭代对象转成集合，如果有重复那么直保留一个

    remove(11) 删除指定的集合
    clear() 清空

    集合相关的操作
        并集，交集，差集

'''

tr1 = {
    'name': '高小一',
    'age': 18,
    'salary': 30000,
    'city': '北京'
}
tr2 = {
    'name': '高小二',
    'age': 19,
    'salary': 20000,
    'city': '上海'
}
tr3 = {
    'name': '高小五',
    'age': 20,
    'salary': 10000,
    'city': '深圳'
}
th = [tr1, tr2, tr3]

for t in th:
    if t.get('salary') > 15000:
        print(t)





