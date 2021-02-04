import os
from modules.local.databaseBasic import dbPath
from modules.local.databaseBasic import createDb, executeSchema
from modules.network.proxy import turnProxy

# Configuration file/directory path.
workingDirectory = os.path.dirname(__file__)
configDirectoryPath = os.path.normpath(os.path.join(workingDirectory, "..", "..", "config"))
apiFilePath = os.path.normpath(os.path.join(workingDirectory, "..", "..", "config", "api.env"))
proxyFilePath = os.path.normpath(os.path.join(workingDirectory, "..", "..", "config", "proxy.conf"))

# Checks if database directory exists/create it.
def createConfigDirectory():
    if os.path.exists(configDirectoryPath):
        print("Configuration directory exists.")
        pass
    else:
        print("Configuration directory doesn't exist. Creating...")
        os.makedirs(configDirectoryPath)
        with open(apiFilePath, "x"):
            pass
        with open(proxyFilePath, "x"):
            pass

def createProxyFile(proxyFilePath):
    with open(proxyFilePath, "a") as f:
        f.write("proxy=FALSE")

# Writes VirusTotal API Key into the api file.
def setApi(key):
    try:
        with open(apiFilePath, "w") as f:
            apiString = "KEY=" + '"' + key + '"'
            f.write(apiString)
    except FileNotFoundError as e:
        print(e)

# Loads API key.
def loadApi():
    try:
        with open(apiFilePath, "r") as f:
            key = f.readline().split('=')[1].strip('"')
        return key
    except FileNotFoundError as e:
        print("Config file not found!")
        print(e)
    except IndexError:
        print("No valid API Key was found.")

# First start checks and tweaks.

def startConfigFiles():
    print("Running initial file checks...")
    # Initial checks - is there config directory, are there config/env files?
    isDirectory = os.path.isdir(configDirectoryPath)
    isEnv = os.path.isfile(apiFilePath)
    isProxy = os.path.isfile(proxyFilePath)
    turnProxy("off")
    if isDirectory == True and isEnv == True and isProxy == True:
        print("All configuration files in place.")
    elif isDirectory == False:
        createConfigDirectory()
        key = input("Enter VT API key:\n> ")
        setApi(key)
        createProxyFile(proxyFilePath)
    elif isEnv == False:
        key = input("Enter VT API Key:\n")
        setApi(key)
        if isProxy == False:
            createProxyFile(proxyFilePath)
        else:
            pass

def startDatabase():
    isDatabase = os.path.isfile(dbPath)
    if isDatabase == True:
        print("There is a database.")
    else:
        print("There is no db. :(")
        createDb()
        executeSchema()
        print("And now there is a db. :)")