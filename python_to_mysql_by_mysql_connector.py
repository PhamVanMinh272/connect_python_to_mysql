# By this script you can connect python to mysql
# make sure you have already had db in mysql
# run: pip install mysql-connector
import mysql.connector

connection = mysql.connector.connect(
  host="localhost", # your host
  user="root", # your db username
  passwd="root", # your db password
  database="demo" # your db name
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM person")
people = cursor.fetchall()
for person in people:
  print(person)