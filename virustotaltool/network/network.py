import requests
import json

from settings.settings import loadApi

def singleUrlScan(resource):
    url = "https://www.virustotal.com/vtapi/v2/url/scan"
    apiKey = loadApi()
    params = {"apikey":apiKey, "url":resource}
    response = requests.post(url, data=params)
    return response

def singleUrlReport(resource):
    url = "https://www.virustotal.com/vtapi/v2/url/report"
    apiKey = loadApi()
    params = {"apikey":apiKey, "url":resource}
    response = requests.post(url, data=params)
    return response