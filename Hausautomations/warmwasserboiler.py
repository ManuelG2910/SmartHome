from datetime import datetime, timedelta
import time

# Default-Wert = aus
aktivierungszeit= None
statusaktiv = True
startzeit = datetime.now()
endzeit = datetime.now()
automaik = False

thisdict = {
    "Laufzeit": 120,
    "Solarstromwerte": 2.0,
    "Tarifzeiten": 4.0,
    "Prüfungszeit": 2.0
}
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
            if datetime.now() > startzeit and datetime.now() < endzeit:
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





