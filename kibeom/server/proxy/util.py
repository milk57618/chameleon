import psutil

def testfunction():
    return True

def getSubnet():
    addrs = psutil.net_if_addrs()
    print(addrs)

getSubnet()