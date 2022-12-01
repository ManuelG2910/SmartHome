from datetime import datetime, timedelta

# Default-Wert = aus
aktivierungszeit= None
statusaktiv = "aus"
startzeit = datetime.now()
endzeit = datetime.now()

thisdict = {
    "Laufzeit": 120,
    "Solarstromwerte": 2.0,
    "Tarifzeiten": 4.0,
    "Prüfungszeit": 2.0
}
def aktivieren():
    statusaktiv= "an"
    print(statusaktiv)
    aktivierungszeit= datetime.now()
    print(aktivierungszeit)

def deaktivieren():
    statusaktiv= "aus"
    print(statusaktiv)
    deaktivierungszeit = datetime.now()
    print(deaktivierungszeit)

def automatik(startzeit, endzeit):
    print(datetime.now().time())
    if datetime.now() > startzeit and datetime.now() < endzeit:
        aktivieren()
    else:
        deaktivieren()
def pruefungszeit_anapssen(pruefungszeit):
    thisdict["Prüfungszeit"] = pruefungszeit

def tarifzeiten_anpassen(tarifzeit):
    thisdict["Tarifzeit"] = tarifzeit

def laufzeit_anpassen(laufzeit):
    thisdict["Laufzeit"] = laufzeit
def solarstromwerte_anpassen(stromwert):
 thisdict["Stromwert"] = stromwert





