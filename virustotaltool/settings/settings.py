import os, sqlite3

configPath = os.path.join(os.getcwd(), "virustotaltool", "settings", "settings.conf")
apiPath = os.path.join(os.getcwd(), "virustotaltool", "settings", "api.env")

def loadApi():
    try:
        with open(apiPath, "r") as f:
            apiKey = f.readline().split('=')[1].strip('"')
        return apiKey
    except FileNotFoundError:
        print("API Key environmental file not found! Creating it right now...")
        os.makedirs(os.path.dirname(apiPath), exist_ok=True)
        with open(apiPath, "w") as f:
            f.write("")
        print("API environmental file created.")
        setApi()
    except IndexError:
        print("No valid API Key was found.")
        setApi()

def setApi():
    print("Enter valid VirusTotal API Key:")
    apiKey = str(input("> "))
    with open(apiPath, "r+") as f:
        f.write("KEY=" + '"' + apiKey + '"')

def changeApi(newKey):
    newKey = str(newKey)
    with open(apiPath, "w") as f:
        f.write("KEY=" + '"' + newKey + '"')