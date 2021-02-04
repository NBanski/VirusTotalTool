import os

workingDirectory = os.path.dirname(__file__)
proxyFilePath = os.path.normpath(os.path.join(workingDirectory, "..", "..", "config", "proxy.conf"))
proxySwitchPath = os.path.normpath(os.path.join(workingDirectory, "..", "..", "config", "proxy.switch"))

def turnProxy(switch):
    with open(proxySwitchPath, "w") as proxySwitch:
        if switch == "on":
            proxySwitch.write("True")
        if switch == "off":
            proxySwitch.write("False")

def checkProxy():
    with open(proxySwitchPath, "r") as proxySwitch:
        if "True" in proxySwitch.read():
            return True
        else:
            return False