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

# Request for a single report.
def getReport(resource):
    url = "https://virustotal.com/vtapi/v2/url/report"
    apiKey = loadApi()
    params = {"apikey": apiKey, "resource": resource}
    response = requests.post(url, data=params)
    return response