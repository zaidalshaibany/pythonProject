import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="zaidPython1",
  password="Noor@@##"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabasepython")
