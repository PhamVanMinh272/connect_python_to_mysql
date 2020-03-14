# By this script you can connect python to mysql
# make sure you have already had db in mysql
# run: pip install pymysql
import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='demo',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()
sql = "select * from person"
cursor.execute(sql)
people = cursor.fetchall()
for person in people:
  print(person)
