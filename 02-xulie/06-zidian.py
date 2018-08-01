# -- coding:utf-8 ----
r1 = {"name": '张三', "age": 18, 'salary': 3000, "city": '北京'}
r2 = {"name": '李四', "age": 19, 'salary': 2000, "city": '北京'}
r3 = {"name": '王五', "age": 20, 'salary': 1000, "city": '北京'}
tb = [r1, r2, r3]
for i in range(len(tb)):
    print(tb[i].get('name'), tb[i].get('age'), tb[i].get('salary'), tb[i].get('city'))