router1 = {
    "2.4G" : 1,
    "5G" : 0,
    "WPA2" : 1,
    "WPA3" : 0,
    "802.11ax" : 1,
    "802.11bgn" : 0,
    "2.4G_WPA2_802.11bgnax" : 0
}

router2 = {
    "2.4G" : 1,
    "5G" : 1,
    "WPA2" : 1,
    "WPA3" : 1,
    "802.11ax" : 1,
    "802.11bgn" : 1,
    "2.4G_WPA2_802.11bgnax" : 1
}

def setRouterValue(router, value, newValue):
    router[value] = newValue

def getRouterValue(router, value):
    return (router[value])