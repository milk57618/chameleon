import socket


def testfunction():
    return True

def getSubnet():
    addrs = socket.if_nameindex()
    return addrs
