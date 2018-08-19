#!/usr/bin/env python3


import requests
import urllib
import re

url = "http://www.wetter.de/deutschland/wetter-nuernberg-18227303.html"
# Wettertypen
sun = "<!-- key: wolke_klein-sonne  -->"
rain = "<!-- key: wolke_klein-sonne  -->"
clouds = "<!-- key: wolke_klein-sonne  -->"
cloudsun = "<!-- key: wolke_klein-sonne  -->"
gewitter = "<!-- key: wolke_klein-sonne  -->"

def scrape():
    print("[+] Reading feed")
    response = requests.get(url)
    html = response.text()
    if sun in html: print("Die Sonne scheint.")
    elif rain in html: print("Es regnet.")
    elif clouds in html: print("Es ist wolkig.")
    elif cloudsun in html: print("Sonne bricht durch die Wolken.")
    elif gewitter in html: print("Es gewittert.")
    else: print("Es gibt kein Wetter. die Welt ist untergegangen.")
