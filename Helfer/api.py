import time
import requests
import os
import locale
from pathlib import Path

from Hausautomations import sturmwarnung
from Hausautomations import infrarotheizung

# Auslesen der Api alle 60 Sekunden und wenn ein neuer Wert rein kam, wird der Wert im Programm weiter verarbeitet


# List die Raumtemperatur und die Luftfeuchtigkeit aus der API vom Hobbyraum aus
def hobbyraum_auslesen():
    # Setzen eines Defaultwertes
    letzte_Auslesung_Hobbyraum = '15.12.2022 09:37:39'

    # Alle 60 Sekunden wird die API ausgelesen
    while True:
        # Aufrufen der API
        response = requests.get("https://measurements.mobile-alerts.eu/Home/SensorsOverview?phoneid=285142992122", headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'})

        # Prüfung ob Datei erolgreich gelöscht wurde, wenn nicht dann wird er gelöscht
        if os.path.exists("HTML\\Hobbyraum.txt"):
            os.remove("HTML\\Hobbyraum.txt")

        # html wird in eine Text-Datei geschrieben
        f = open("HTML\\Hobbyraum.txt", "x")
        f.write(str(response.content.decode()))
        f.close()
        f = open("HTML\\Hobbyraum.txt")

        # Text-Datei wird ausglesen, die Zeilen 922, 930, 946
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


# List die Wingeschwindigkeit und die Windrichtung aus. Wenn ein neuer Wert rein kam, wird dieser vom Programm weiter verarbeitet
def windsensor_auslesen():
    # Setzen eines Defaultwertes
    letzte_Auslesung_Windsensor = '15.12.2022 09:37:39'

    # Alle 60 Sekunden wird die API ausgelesen
    while True:
        # Aufrufen der API
        response = requests.get("https://measurements.mobile-alerts.eu/Home/SensorsOverview?phoneid=285142992122", headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'})

        # Prüfung ob Datei erolgreich gelöscht wurde, wenn nicht dann wird er gelöscht
        file = "HTML\\Windsensor.txt"
        if os.path.exists("HTML\\Windsensor.txt"):
            os.remove("HTML\\Windsensor.txt")

        # html wird in eine Text-Datei geschrieben
        f = open("HTML\\Windsensor.txt", "x")
        f.write(str(response.content.decode()))
        f.close()
        f = open("HTML\\Windsensor.txt")

        # Text-Datei wird ausglesen, die Zeilen 922, 930, 946
        content = f.readlines()

        zeitpunkt = content[922].split("<h4>")[1].split("</h4>")[0]                 # entfernen der html Zeichen
        windgeschwindigkeit = content[930].split("<h4>")[1].split("</h4>")[0]       # entfernen der html Zeichen
        windgeschwindigkeit = windgeschwindigkeit.split(' km/h')[0]                 # entfernen der km/h
        windrichtung = content[946].split("<h4>")[1].split("</h4>")[0]              # entfernen der html Zeichen

        # Prüfung, ob es neue Werte gibt anhand der Uhrzeit
        if str(letzte_Auslesung_Windsensor) is not str(zeitpunkt):

            # Temperatur in float umwandeln
            locale.setlocale(locale.LC_ALL, 'nl_NL')
            windgeschwindigkeit = locale.atof(windgeschwindigkeit)

            # Werte an das Programm weitergeben
            sturmwarnung.schwellenwert_Strumwarnung_pruefen(windgeschwindigkeit, windrichtung)

            # neuer letzter Zeitpunkt wird gesetzt
            letzte_Auslesung_Windsensor = zeitpunkt

            print(zeitpunkt)

        # Datei schließen und löschen
        f.close()
        os.remove("HTML\\Windsensor.txt")

        # Methode eine Minute schlafen lassen
        time.sleep(60)