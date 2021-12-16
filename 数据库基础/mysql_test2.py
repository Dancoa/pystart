# 在数据库建表
import mysql.connector
conn = mysql.connector.connect(user='root', password='woshialex_3', database='python_test')
cursor = conn.cursor()
cursor.execute('create table lesson (\
    ID varchar(20) primary key, \
    name varchar(20))')
cursor.close()
conn.close()