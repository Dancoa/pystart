import mysql.connector
conn = mysql.connector.connect(user='root',password='woshialex_3',database='python_test')
cursor = conn.cursor()
# cursor.execute('create table study2 (ID int primary key,name varchar(20))')
cursor.execute('insert into study2 (ID,name) values (%s,%s)',[1,'mike'])
cursor.execute('insert into study2 (ID,name) values (%s,%s)',[2,'like'])

conn.commit()
cursor.execute('select * from study2')
values = cursor.fetchall()
print(values)

cursor.close
conn.close