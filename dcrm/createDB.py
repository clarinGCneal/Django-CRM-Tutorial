import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Necronomicon",
)

# prepare a cursor object
cursorObject = database.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE User1")

print("Database created successfully")