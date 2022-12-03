import time
from Helfer import whatsapp_nachricht

anzahl_Mobilnummer = 0

thisdict = {
    "Schwellenert_Strumwarnung": 3.0,
    "Nachricht Sturmwarnung": "Achtung, starker Wind! Ist alles sicher?"
}

# Neue Mobilnummer zu Dictionary hinzufügen
def mobilnummer_hinzufuegen(mobilnummer):
    anzahl_Mobilnummer =+1
    thisdict["Handynummer" + str(anzahl_Mobilnummer)] = mobilnummer

# Vorhandene Mobilnummer in Dictionary anpassen
def mobilnummer_aendern(mobilnummer_alt, mobilnummer_neu):
    key = thisdict.values(mobilnummer_alt)
    thisdict[key] = mobilnummer_neu

# Vorhandene Mobilnummer löschen
def mobilnummer_loeschen(mobilnummer):
    key = thisdict.values(mobilnummer)
    del thisdict[key]

# Stellenwert in Dictionary anpassen
def schwellenwert_Strumwarnung_aendern( schwellenwert_Sturm):
    thisdict["Schwellenert_Strumwarnung"] = schwellenwert_Sturm

# aktueller Windwert wird mit dem Stellenwert abgeglichen und ggf wird eine Nahcricht versendet
def schwellenwert_Strumwarnung_pruefen():
    while True:
        windwert = 0 # ruft Methode zu windwert auf
        if thisdict["Schwellenert_Strumwarnung"] >= windwert:
            whatsapp_nachricht.nachricht_senden(thisdict["Handynummer"], thisdict["Nachricht Sturmwarnung"])
        print("Thread_1")
        time.sleep(60)

# Nachricht wird bei Sturmwarnung versendet
