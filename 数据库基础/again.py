import mysql.connector
conn = mysql.connector.connect(user='root',password='woshialex_3',database='python_test')
cursor = conn.cursor()
# cursor.execute('create table xman (ID int primary key,name varchar(20))')
# cursor.execute('insert into xman (ID,name) values (%s,%s)',[1,'batman'])
# cursor.execute('insert into xman (ID,name) values (%s,%s)',[2,'superman'])
# cursor.execute('insert into xman (ID,name) values (%s,%s)',[3,'ironman'])

# conn.commit()
cursor.execute('select * from xman')
values = cursor.fetchall()
print(values)

for x in values:
    print(x)

cursor.close()
conn.close()