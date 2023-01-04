import time
from Helfer import whatsapp_nachricht

thisdict = {
    "Schwellenert_Strumwarnung": 3.0,
    "Nachricht Sturmwarnung": "Achtung, starker Wind! Ist alles sicher?"
}


# Stellenwert in Dictionary anpassen
def schwellenwert_Strumwarnung_aendern( schwellenwert_Sturm):
    thisdict["Schwellenert_Strumwarnung"] = schwellenwert_Sturm

# aktueller Windwert wird mit dem Stellenwert abgeglichen und ggf wird eine Nahcricht versendet


def schwellenwert_Strumwarnung_pruefen(windgeschwindigkeit, windrichtung):

    print('Thread 4')

    if thisdict["Schwellenert_Strumwarnung"] >= float(windgeschwindigkeit):
        print('Nachricht')
        #whatsapp_nachricht.nachricht_senden(windgeschwindigkeit, windrichtung)
