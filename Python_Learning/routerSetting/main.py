from routerSupportTable import *

def AP_24G_WPA2():
    return
    # print("AP_24G_WPA2")

def AP_24G80211ax():
    return
    # print("AP_24G80211ax")

def AP_24G80211bgn():
    return
    # print("AP_24G80211bgn")

def AP_24G80211bgnax():
    return
    # print("AP_24G80211bgnax")

def AP_24GWPASSIDConnect():
    return
    # print("AP_24GWPASSIDConnect")

def WifiTriggerOnOff():
    return
    # print("WifiTriggerOnOff")

def DCTriggerOnOff():
    return
    # print("DCTriggerOnOff")

def ACTriggerOnOff():
    return
    # print("ACTriggerOnOff")

def AP_WIFI_TriggerOnOff():
    return
    # print("AP_WIFI_TriggerOnOff")

def AP_24G_WPA3():
    return

def AP_5G_WPA2():
    return

def AP_5G_WPA3():
    return

def AP_5G80211ax():
    return

def AP_5GWPASSIDConnect():
    return

def AP_5G80211ac():
    return

def AP_5G80211a():
    return

WifiEventList = [
    ["001_TV_Wifi_Off/On_", "002_DC_", "003_AC_", "004_AP_Power_", "2.4G_WPA2_802.11ax",
                AP_24G_WPA2, AP_24G80211ax, AP_24GWPASSIDConnect, WifiTriggerOnOff, DCTriggerOnOff, ACTriggerOnOff, AP_WIFI_TriggerOnOff],
    ["005_TV_Wifi_Off/On_", "006_DC_", "007_AC_", "008_AP_Power_", "2.4G_WPA2_802.11bgn",
                AP_24G_WPA2, AP_24G80211bgn, AP_24GWPASSIDConnect, WifiTriggerOnOff, DCTriggerOnOff, ACTriggerOnOff, AP_WIFI_TriggerOnOff],
    ["009_TV_Wifi_Off/On_", "010_DC_", "011_AC_", "012_AP_Power_", "2.4G_WPA2_802.11bgnax",
                AP_24G_WPA2, AP_24G80211bgnax, AP_24GWPASSIDConnect, WifiTriggerOnOff, DCTriggerOnOff, ACTriggerOnOff, AP_WIFI_TriggerOnOff],
    ["013_TV_Wifi_Off/On_", "014_DC_", "015_AC_", "016_AP_Power_", "2.4G_WPA3_802.11ax",
                AP_24G_WPA3, AP_24G80211ax, AP_24GWPASSIDConnect, WifiTriggerOnOff, DCTriggerOnOff, ACTriggerOnOff, AP_WIFI_TriggerOnOff],
    ["017_TV_Wifi_Off/On_", "018_DC_", "019_AC_", "020_AP_Power_", "2.4G_WPA3_802.11bgn",
                AP_24G_WPA3, AP_24G80211bgn, AP_24GWPASSIDConnect, WifiTriggerOnOff, DCTriggerOnOff, ACTriggerOnOff, AP_WIFI_TriggerOnOff],
    ["021_TV_Wifi_Off/On_", "022_DC_", "023_AC_", "024_AP_Power_", "2.4G_WPA3_802.11bgnax",
                AP_24G_WPA3, AP_24G80211bgnax, AP_24GWPASSIDConnect, WifiTriggerOnOff, DCTriggerOnOff, ACTriggerOnOff, AP_WIFI_TriggerOnOff],
    ["025_TV_Wifi_Off/On_", "026_DC_", "027_AC_", "028_AP_Power_", "5G_WPA2_802.11ax",
                AP_5G_WPA2, AP_5G80211ax, AP_5GWPASSIDConnect, WifiTriggerOnOff, DCTriggerOnOff, ACTriggerOnOff, AP_WIFI_TriggerOnOff],
    ["029_TV_Wifi_Off/On_", "030_DC_", "031_AC_", "032_AP_Power_", "5G_WPA2_802.11ac",
                AP_5G_WPA2, AP_5G80211ac, AP_5GWPASSIDConnect, WifiTriggerOnOff, DCTriggerOnOff, ACTriggerOnOff, AP_WIFI_TriggerOnOff],
    ["033_TV_Wifi_Off/On_", "034_DC_", "035_AC_", "036_AP_Power_", "5G_WPA2_802.11a",
                AP_5G_WPA2, AP_5G80211a, AP_5GWPASSIDConnect, WifiTriggerOnOff, DCTriggerOnOff, ACTriggerOnOff, AP_WIFI_TriggerOnOff],
    ["037_TV_Wifi_Off/On_", "038_DC_", "039_AC_", "040_AP_Power_", "5G_WPA3_802.11ax",
                AP_5G_WPA3, AP_5G80211ax, AP_5GWPASSIDConnect, WifiTriggerOnOff, DCTriggerOnOff, ACTriggerOnOff, AP_WIFI_TriggerOnOff],
    ["041_TV_Wifi_Off/On_", "042_DC_", "043_AC_", "044_AP_Power_", "5G_WPA3_802.11ac",
                AP_5G_WPA3, AP_5G80211ac, AP_5GWPASSIDConnect, WifiTriggerOnOff, DCTriggerOnOff, ACTriggerOnOff, AP_WIFI_TriggerOnOff],
    ["045_TV_Wifi_Off/On_", "046_DC_", "047_AC_", "048_AP_Power_", "5G_WPA3_802.11a",
                AP_5G_WPA3, AP_5G80211a, AP_5GWPASSIDConnect, WifiTriggerOnOff, DCTriggerOnOff, ACTriggerOnOff, AP_WIFI_TriggerOnOff]
]

def run(routerName):
    CheckNumber = len(WifiEventList)
    for CheckIndex in range(0, CheckNumber, 1):
        run = (getRouterValue(routerName, WifiEventList[CheckIndex][4].split("_")[0]) +
               getRouterValue(routerName, WifiEventList[CheckIndex][4].split("_")[1]) +
               getRouterValue(routerName, WifiEventList[CheckIndex][4].split("_")[2]))

        if (run == 3):
            for wifiEvent in range (5, 12):
                if (wifiEvent == 8):
                    WifiEventList[CheckIndex][wifiEvent]()
                    print(WifiEventList[CheckIndex][wifiEvent])
                elif (wifiEvent == 9):
                    WifiEventList[CheckIndex][wifiEvent]()
                    print(WifiEventList[CheckIndex][wifiEvent])
                elif (wifiEvent == 10):
                    WifiEventList[CheckIndex][wifiEvent]()
                    print(WifiEventList[CheckIndex][wifiEvent])
                elif (wifiEvent == 11):
                    WifiEventList[CheckIndex][wifiEvent]()
                    print(WifiEventList[CheckIndex][wifiEvent])
                else:
                    WifiEventList[CheckIndex][wifiEvent]()
                    print(WifiEventList[CheckIndex][wifiEvent])

        print("===========================")