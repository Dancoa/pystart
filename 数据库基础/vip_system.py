# 在数据库中写入表，插入数据，然后查询表中的数据
import mysql.connector
conn = mysql.connector.connect(user='root', password='woshialex_3', database='python_test')
cursor = conn.cursor()
cursor.execute('create table userInfo (\
    ID varchar(20) primary key, \
    name varchar(20))')

cursor.execute('insert into userInfo (ID, name) values (%s, %s)', ['001', 'danco'])
cursor.execute('insert into userInfo (ID, name) values (%s, %s)', ['002', 'alex'])
cursor.execute('insert into userInfo (ID, name) values (%s, %s)', ['003', 'oreo'])

conn.commit()
cursor.close()
conn.close()