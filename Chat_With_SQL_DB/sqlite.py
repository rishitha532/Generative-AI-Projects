import sqlite3

## connect to sqlite
connection=sqlite3.connect("student.db")

##create a cursor object to insert record, create table
cursor=connection.cursor()

## create the table
table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(table_info)

## Insert some more records
cursor.execute('''Insert Into STUDENT values('Kiran','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Bumrah','Data Analytics','A',100)''')
cursor.execute('''Insert Into STUDENT values('Kohli','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Rohit','DEVOPS','E',50)''')
cursor.execute('''Insert Into STUDENT values('Maxwell','Computer Engineering','C',78)''')
cursor.execute('''Insert Into STUDENT values('Buttler','Mathematics','B',82)''')
cursor.execute('''Insert Into STUDENT values('Markram','Finance','D',64)''')
cursor.execute('''Insert Into STUDENT values('Siraj','Computer Science','D',67)''')
cursor.execute('''Insert Into STUDENT values('Gill','MIS','F',35)''')


## Display all the records
print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes in the database
connection.commit()
connection.close()