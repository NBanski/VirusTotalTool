import requests
import json

from VirusTotalTool.modules.local.settings import loadApi

# Request to perform a scan.
def getUrlScan(resource):
    url = "https://virustotal.com/vtapi/v2/url/scan"
    apiKey = loadApi()
    params = {"apikey": apiKey, "url": resource}
    response = requests.post(url, data=params)
    return response

# Request for a single report.
def getReport(resource):
    url = "htts://virustotal.com/vtapi/v2/url/report"
    apiKey = loadApi()
    params = {"apikey": apiKey, "url": resource}
    response = requests.post(url, data=params)
    return response