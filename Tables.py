import mysql.connector

# Establish the database connection
mydb = mysql.connector.connect(host="localhost", user="root", passwd="")
mycursor = mydb.cursor()

# Create the database if it doesn't exist
mycursor.execute("CREATE DATABASE IF NOT EXISTS Library")
mydb.database = "Library"  # Set the database context

# Create BookRecord table if it doesn't exist
mycursor.execute("SHOW TABLES LIKE 'BookRecord'")
if not mycursor.fetchone():
    mycursor.execute(
        """CREATE TABLE BookRecord(
            BookID varchar(10) PRIMARY KEY, 
            BookName varchar(35), 
            Author varchar(30), 
            Publisher varchar(30)
        )"""
    )

# Create UserRecord table if it doesn't exist
mycursor.execute("SHOW TABLES LIKE 'UserRecord'")
if not mycursor.fetchone():
    mycursor.execute(
        """CREATE TABLE UserRecord(
            UserID varchar(10) PRIMARY KEY, 
            UserName varchar(20),
            Password varchar(20), 
            BookID varchar(10),
            FOREIGN KEY (BookID) REFERENCES BookRecord(BookID)
        )"""
    )
    # Insert data into UserRecord table
    data1 = ("101", "Kunal", "1234", None)
    data2 = ("102", "Vishal", "3050", None)
    data3 = ("103", "Siddhesh", "5010", None)
    query1 = "INSERT INTO UserRecord VALUES(%s, %s, %s, %s)"
    mycursor.execute(query1, data1)
    mycursor.execute(query1, data2)
    mycursor.execute(query1, data3)
    mydb.commit()

# Create AdminRecord table if it doesn't exist
mycursor.execute("SHOW TABLES LIKE 'AdminRecord'")
if not mycursor.fetchone():
    mycursor.execute(
        """CREATE TABLE AdminRecord(
            AdminID varchar(10) PRIMARY KEY, 
            Password varchar(20)
        )"""
    )
    # Insert data into AdminRecord table
    data4 = ("Kunal1020", "123")
    data5 = ("Siddesh510", "786")
    data6 = ("Vishal305", "675")
    query2 = "INSERT INTO AdminRecord VALUES(%s, %s)"
    mycursor.execute(query2, data4)
    mycursor.execute(query2, data5)
    mycursor.execute(query2, data6)
    mydb.commit()

# Create Feedback table if it doesn't exist
mycursor.execute("SHOW TABLES LIKE 'Feedback'")
if not mycursor.fetchone():
    mycursor.execute(
        """CREATE TABLE Feedback(
            Feedback varchar(100) PRIMARY KEY, 
            Rating varchar(10)
        )"""
    )

# Close the cursor and database connection
mycursor.close()
mydb.close()
