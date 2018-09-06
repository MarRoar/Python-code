import pymysql

conn = pymysql.connect(host = 'localhost', user="root", password="123456", db="test", charset="utf8")

cur = conn.cursor()

sql = "INSERT INTO users(username, password, age, ses) VALUE('chow', '123', 45, 1);"

cur.execute(sql)
conn.commit()

cur.close()

conn.close()