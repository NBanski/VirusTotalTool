import requests, os

from requests.auth import HTTPProxyAuth

workingDirectory = os.path.dirname(__file__)
proxyFilePath = os.path.normpath(os.path.join(workingDirectory, "..", "..", "config", "proxy.conf"))

def writeProxyProtocol(protocol):
    with open(proxyFilePath, "a") as f:
        f.append(protocol)