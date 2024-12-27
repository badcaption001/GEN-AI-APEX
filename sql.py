import sqlite3
connection=sqlite3.connect("student.db")
cursor=connection.cursor()
cursor.execute("""create table Student(NAME varchar(20),CLASS varchar(20),SECTION varchar(10),MARK INT) """)

#insert values into table

cursor.execute(""" insert into student values("sathishsivam","Datascience","A",78)""")
cursor.execute(""" insert into student values("Mani","Datascience","A",98)""")
cursor.execute(""" insert into student values("Kumar","DevOps","B",68)""")
cursor.execute(""" insert into student values("Rajesh","Java","C",48)""")
cursor.execute(""" insert into student values("Ramesh","DevOps","B",98)""")

# res=cursor.execute(""" select * from student where class=='DevOps'""")
# for i in res:
#     print(i)