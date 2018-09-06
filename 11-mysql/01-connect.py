import pymysql

conn = pymysql.connect(host = 'localhost', user="root", password="123456", db="test", charset="utf8")

cur = conn.cursor()

sql = 'SELECT * FROM users'

cur.execute(sql)

emps = cur.fetchall()

for i in emps:
    print(i)


cur.close()

conn.close()