import os, sqlite3

from sqlite3 import Error

# Database/db directory path.
workingDirectory = os.path.dirname(__file__)
directoryPath = os.path.normpath(os.path.join(workingDirectory, "..", "..", "database"))
dbPath = os.path.normpath(os.path.join(workingDirectory, "..", "..", "database", "vttool.db"))

# Schema.sql path.
schemaPath = os.path.normpath(os.path.join(workingDirectory, "..", "..", "database", "schema.sql"))

# Check if database directory exists/create it.
def createDbDirectory():
    if os.path.exists(directoryPath):
        print("Database directory exists.")
        pass
    else:
        print("Database directory doesn't exist. Creating...")
        os.makedirs(directoryPath)

# Check if database exists/create it.
def createDb():
    conn = None
    try:
        conn = sqlite3.connect(dbPath)
        print(sqlite3.version)
        print("Database succesfully connected.")
    except Exception as e:
        print(e)
    finally:
        if conn:
            conn.close()

# Connect to the database.
def connectDb():
    connection = None
    try:
        connection = sqlite3.connect(dbPath)
    except Error as e:
        print(e)
    return connection

# Initialise database.
# Erase tables, create new ones.
def executeSchema():
    try:
        db = connectDb()
        with open(schemaPath, "r") as f:
            db.executescript(f.read())
    except FileNotFoundError as e:
        print(os.getcwd())
        print(os.listdir())
        print(e)
    