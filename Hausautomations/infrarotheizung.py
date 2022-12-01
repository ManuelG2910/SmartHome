from datetime import datetime, timedelta
import time

# Steuerung der Infrarotheizung

aktivierte_Heizung_Zeit = None
max_heiz_Zeit = None
pause_Zeit = None

thisdict = {
    "Schwellenwert Luftfeuchtigkeit": 3.0,
    "Schwellenwert Temperatur": 3.0,
    "Laufzeit": 120,
    "Laufzeit Pause": 15,
    "Heizung automatisch": True,
    "Prüfungszeit": 5,
    "Balkonkraftwerk Strom Wert": 300,
}


# Heizung wird aktiviert mit Maximum Laufzeit berechnung
def heizung_aktivieren():
    aktuelle_Zeit = datetime. datetime. jetzt()
    dt = datetime.strptime(aktuelle_Zeit, '%Y-%m-%d %H:%M:%S.%f')
    max_heiz_Zeit = dt+timedelta(minutes=float(thisdict["Laufzeit"]))


# Heizung wird deaktiviert mit Pausenberechnung
def heizung_deaktivieren():
    max_heiz_Zeit = 0
    print()

# Automatisiertes Heizen
def heizung_automatisch_aktivieren():
    thisdict["Heizung automatisch"] = True

# nicht Automatisiertes Heizen
def heizung_automatisch_deaktivieren():
    thisdict["Heizung automatisch"] = False

def laufzeit_pruefen():
    while True:
        aktuelle_Zeit = datetime.datetime.jetzt()
        if aktuelle_Zeit > max_heiz_Zeit:
            heizung_deaktivieren()
            time.sleep(thisdict["Prüfungszeit"]*60)

    time.sleep(60)
def balkonkraftwerk_strom_pruefung():
    x = 0# Methode in für  Balkonkraftwerk Strom aufrufen

    if x > thisdict["Balkonkraftwerk Strom Wert"]:
        heizung_automatisch_aktivieren()
    else:
        heizung_automatisch_deaktivieren()

    time.sleep(thisdict["Balkonkraftwerk Strom Wert"]*60)

def optimiertes_Heizen():
    aktuelle_Temp = 0 # aktuelle Zimmertemperatur holen
    aktuelle_Luftf = 0 # aktuelle Luftfeuchtigkeit holen

    if aktuelle_Temp < ["Schwellenwert Temperatur"] and aktuelle_Luftf > ["Schwellenwert Luftfeuchtigkeit"]:
        heizung_aktivieren()
    elif aktuelle_Temp > ["Schwellenwert Temperatur"] and aktuelle_Luftf < ["Schwellenwert Luftfeuchtigkeit"]:
        heizung_deaktivieren()

    time.sleep(60)

# Laufzeit anpassen
def laufzeit_anpassen(laufzeit):
    thisdict["Laufzeit"] = laufzeit

# Laufzeit Pause anpassen
def laufzeit_pause_anpassen(laufzeit_pause):
    thisdict["Laufzeit Pause"] = laufzeit_pause

# Prüfungszeiten anpassen
def pruefungszeit_anpassen(pruefungszeit):
    thisdict["Prüfungszeit"] = pruefungszeit

# Balkonkraftwerk Strom anpassen
def balkonkraftwer_strom_anpassen(balkonkraftwer_strom):
    thisdict["Balkonkraftwerk Strom"] = balkonkraftwer_strom

# Schwellenwert Luftfeuchtigkeit anpassen
def schwellwert_luftfeuchtigkeit_anpassen(luftfeuchtigkeit):
    thisdict["Schwellenwert Luftfeuchtigkeit"] = luftfeuchtigkeit

# Schwellenwert Temperatur anpassen
def schwellwert_temperatur_anpassen(temperatur):
    thisdict["Schwellenwert Temperatur"] = temperatur

