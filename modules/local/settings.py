import os

# Configuration file/directory path.
workingDirectory = os.path.dirname(__file__)
configDirectory = os.path.normpath(os.path.join(workingDirectory, "..", "..", "config"))
keyPath = os.path.normpath(os.path.join(workingDirectory, "..", "..", "config", "api.env"))

# Check if database directory exists/create it.
def createConfigDirectory():
    if os.path.exists(configDirectory):
        print("Configuration directory exists.")
        pass
    else:
        print("Configuration directory doesn't exist. Creating...")
        os.makedirs(configDirectory)

# Check if database directory exists/create it.
def createApiFile():
    if os.path.exists(keyPath):
        print("API key file exists.")
        pass
    else:
        print("API key file does not exist. Creating...")
        with open(keyPath, "a"):
            pass

# Write VirusTotal API Key into the api file.
def setApi(key):
    try:
        with open(keyPath, "w") as f:
            apiString = "KEY=" + '"' + key + '"'
            f.write(apiString)
    except FileNotFoundError as e:
        print(e)

def loadApi():
    try:
        with open(keyPath, "r") as f:
            key = f.readline().split('=')[1].strip('"')
            return key
    except FileNotFoundError as e:
        print("Api key file not found!")
        print(e)
    except IndexError:
        print("No valid API Key was found.")