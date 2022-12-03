from datetime import datetime, timedelta
import time
import datetime

# Default-Wert = aus
aktivierungszeit= None
statusaktiv = True
automaik = False

thisdict = {
    "Laufzeit": 120,
    "Solarstromwerte": 2.0,
    "Tarifzeiten": 4.0,
    "Prüfungszeit": 2.0,
    "Startzeitraum": "02.12.2022",
    "Endezeitraum": "02.02.2023"
}

startzeit = datetime.datetime(2022, 12, 2)
print(startzeit)
def aktivieren():
    statusaktiv= True
    aktivierungszeit= datetime.now()
    print(aktivierungszeit)

def deaktivieren():
    statusaktiv= False
    deaktivierungszeit = datetime.now()
    print(deaktivierungszeit)

def fall_2_automatisch():
    automatik=True

def fall_4_Solar():
    while True:
        x = 500 # holen der Watt Solarstrom
        if x > 500 and automaik == False: # Ergänzung Uhrzeit
            aktivieren()
        print("Thread_6")
        time.sleep(60*5)
def automatik():
    # holen der start und endzeit
    while True:
        if automatik == True:
            if datetime.now() > startzeit and datetime.now() < startzeit:
                aktivieren()
            else:
                deaktivieren()

        print("Thread_5")
        time.sleep(60*60*12)

def pruefungszeit_anapssen(pruefungszeit):
    thisdict["Prüfungszeit"] = pruefungszeit

def tarifzeiten_anpassen(tarifzeit):
    thisdict["Tarifzeit"] = tarifzeit

def laufzeit_anpassen(laufzeit):
    thisdict["Laufzeit"] = laufzeit
def solarstromwerte_anpassen(stromwert):
 thisdict["Stromwert"] = stromwert





