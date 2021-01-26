import requests
import json

from modules.local.settings import loadApi

# Request to perform a scan.
def getUrlScan(urlToScan):
    url = "https://virustotal.com/vtapi/v2/url/scan"
    apiKey = loadApi()
    params = {"apikey": apiKey, "url": urlToScan}
    response = requests.post(url, data=params)
    return response

# Request for a single report for URL or ID.
def getReport(resource):
    url = "https://virustotal.com/vtapi/v2/url/report"
    apiKey = loadApi()
    params = {"apikey": apiKey, "resource": resource}
    response = requests.post(url, data=params)
    return response

# Request for a single report.
def getFileReport(fileHash):
    url = "https://virustotal.com/vtapi/v2/file/report"
    apiKey = loadApi()
    params = {"apikey": apiKey, "resource": fileHash}
    response = requests.post(url, data=params)
    return response

# Sending a file with POST request.
def getFileScan(filePath):
    url = "https://www.virustotal.com/vtapi/v2/file/scan"
    apiKey = loadApi()
    params = {"apikey": apiKey}
    files = {"file": (filePath, open(filePath, "rb"))}
    response = requests.post(url, files=files, params=params)
    print(response.json())
    return response