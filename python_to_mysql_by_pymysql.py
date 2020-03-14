# By this script you can connect python to mysql
# make sure you have already had db in mysql
# run: pip install pymysql
import pymysql.cursors

connection = pymysql.connect(host='localhost', # your host
                             user='root', # your db username
                             password='root', # your db password
                             db='demo', # your db name
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()
sql = "select * from person"
cursor.execute(sql)
people = cursor.fetchall()
for person in people:
  print(person)
