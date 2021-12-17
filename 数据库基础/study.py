# 构造一个数据库study，创建hello的表，在表中写入数据，查询表中数据
import mysql.connector
conn = mysql.connector.connect(user='root',password='woshialex_3',database='study')
cursor = conn.cursor()
# cursor.execute('create table hello ( \
#     ID int primary key not null, \
#     name varchar(20))')
# cursor.execute('insert into hello (ID,name) values (%s,%s)',[ 1 ,'danco'])    # 无论是字符串、数字、日期、时间，都要用%s
# cursor.execute('insert into hello (ID,name) values (%s,%s)',[ 2 ,'alex'])

conn.commit()   # 一定要有commit，否则插入不生效

cursor.execute('select * from hello')
values = cursor.fetchall()
print(values)

