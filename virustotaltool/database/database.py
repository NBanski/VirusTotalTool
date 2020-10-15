import os, sqlite3, json
from sqlite3 import Error

from network.network import singleUrlScan, singleUrlReport

databaseDirectory = os.path.join(os.getcwd(), "data")
databasePath = os.path.join(os.getcwd(), "data", "vtool_database.db")
schemaPath = os.path.join(os.getcwd(), "virustotaltool", "database", "schema.sql")

def createDirectory():
    if os.path.isdir(databaseDirectory):
        pass
    else:
        os.makedirs(databaseDirectory)

def getDb():
    connection = None
    try:
        connection = sqlite3.connect(databasePath)
    except Error as e:
        print(e)
    return connection

def initDb():
    createDirectory()
    db = getDb()
    with open(schemaPath) as f:
        db.executescript(f.read())