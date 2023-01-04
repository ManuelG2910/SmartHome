import time
import requests
import os
import locale
from pathlib import Path

from Hausautomations import sturmwarnung
from Hausautomations import infrarotheizung






def hobbyraum_auslesen():
    letzte_Auslesung_Hobbyraum = '15.12.2022 09:37:39'
    while True:
        response = requests.get("https://measurements.mobile-alerts.eu/Home/SensorsOverview?phoneid=285142992122", headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'})

        # Prüfung ob Datei erolgreich gelöscht wurde, wenn nicht dann wird er gelöscht

        if os.path.exists("HTML\\Hobbyraum.txt"):
            os.remove("HTML\\Hobbyraum.txt")

        f = open("HTML\\Hobbyraum.txt", "x")
        f.write(str(response.content.decode()))
        f.close()
        f = open("HTML\\Hobbyraum.txt")

        content = f.readlines()

        zeitpunkt = content[442].split("<h4>")[1].split("</h4>")[0]
        temperatur = content[450].split("<h4>")[1].split("</h4>")[0]
        temperatur = temperatur.split(' C')[0]
        luftfeuchtigkeit = content[458].split("<h4>")[1].split("</h4>")[0]
        luftfeuchtigkeit = luftfeuchtigkeit.split('%')[0]

        if str(letzte_Auslesung_Hobbyraum) is not str(zeitpunkt):
            # Temperatur in float umwandeln
            locale.setlocale(locale.LC_ALL, 'nl_NL')
            temperatur = locale.atof(temperatur)

            infrarotheizung.optimiertes_Heizen(temperatur,luftfeuchtigkeit)

            letzte_Auslesung_Hobbyraum = zeitpunkt
            print(zeitpunkt)


        # letzte_Auslesung_Hobbyraum = zeitpunkt

        f.close()
        os.remove("HTML\\Hobbyraum.txt")

        time.sleep(60)

def windsensor_auslesen():
    letzte_Auslesung_Windsensor = '15.12.2022 09:37:39'
    while True:
        response = requests.get("https://measurements.mobile-alerts.eu/Home/SensorsOverview?phoneid=285142992122", headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'})

        # Prüfung ob Datei erolgreich gelöscht wurde, wenn nicht dann wird er gelöscht
        file = "HTML\\Windsensor.txt"
        if os.path.exists("HTML\\Windsensor.txt"):
            os.remove("HTML\\Windsensor.txt")

        f = open("HTML\\Windsensor.txt", "x")
        f.write(str(response.content.decode()))
        f.close()
        f = open("HTML\\Windsensor.txt")

        content = f.readlines()

        zeitpunkt = content[922].split("<h4>")[1].split("</h4>")[0]
        windgeschwindigkeit = content[930].split("<h4>")[1].split("</h4>")[0]
        windgeschwindigkeit = windgeschwindigkeit.split(' km/h')[0]
        windrichtung = content[946].split("<h4>")[1].split("</h4>")[0]


        if str(letzte_Auslesung_Windsensor) is not str(zeitpunkt):
            # Temperatur in float umwandeln
            locale.setlocale(locale.LC_ALL, 'nl_NL')
            windgeschwindigkeit = locale.atof(windgeschwindigkeit)
            sturmwarnung.schwellenwert_Strumwarnung_pruefen(windgeschwindigkeit, windrichtung)

            letzte_Auslesung_Windsensor = zeitpunkt

            print(zeitpunkt)

        f.close()

        os.remove("HTML\\Windsensor.txt")

        time.sleep(60)