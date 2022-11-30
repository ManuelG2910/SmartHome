from datetime import datetime, timedelta
import time

# Steuerung der Infrarotheizung
class infrarotheizung:

    def __init__(self):
        self.heizungAktivierung = None
        self.heizungDeaktivierung = None
        self.heizungPause = None

        self.thisdict = {
            "Schwellenwert Luftfeuchtigkeit": 3.0,
            "Schwellenwert Temperatur": 3.0,
            "Laufzeit": 120,
            "Laufzeit Pause": 15,
            "Heizung automatisch": True,
            "Prüfungszeit": 5,
            "Balkonkraftwerk Strom Wert": 300
        }

    # Heizung wird aktiviert mit Maximum Laufzeit berechnung
    def heizung_aktivieren(self):
        if datetime(infrarotheizung.heizungPause) < datetime.datetime.now():
            # Zeit der Aktivierung speichern, nach x Minuten ausschalten
            heizungAktivierung = datetime.datetime.now()
            dt = datetime.strptime(heizungAktivierung, '%Y-%m-%d %H:%M:%S.%f')
            heizungDeaktivierung = dt + timedelta(minutes=float(infrarotheizung.laufzeit))
        else:
            return False

    # Heizung wird deaktiviert mit Pausenberechnung
    def heizung_deaktivieren(self):
        heizungDeaktivierung = datetime.datetime.now()
        dt = datetime.strptime(heizungDeaktivierung, '%Y-%m-%d %H:%M:%S.%f')
        heizungPause = dt + timedelta(minutes=float(infrarotheizung.pruefungszeit))
        # die Zeit zurück auf 0 setzen

        heizungAktivierung = 0
        heizungDeaktivierung = 0

    # Automatisiertes Heizen
    def heizung_automatisch_aktivieren(self):
        thisdict["Heizung automatisch"] = True
    def heizung_automatisch_deaktivieren(self):
        thisdict["Heizung automatisch"] = False
    def balkonkraftwerk_strom_pruefung(self):
        x = 0# Methode in für  Balkonkraftwerk Strom aufrufen

        if x > thisdict["Balkonkraftwerk Strom Wert"]:
            heizung_automatisch_aktivieren(self)
        else:
            heizung_automatisch_deaktivieren(self)

        time.sleep(thisdict["Balkonkraftwerk Strom Wert"]*60)

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
    def schwellwert_luftfeuchtigkeit_anpassen(self, luftfeuchtigkeit):
        thisdict["Schwellenwert Luftfeuchtigkeit"] = luftfeuchtigkeit

    # Schwellenwert Temperatur anpassen
    def schwellwert_temperatur_anpassen(self, temperatur):
        thisdict["Schwellenwert Temperatur"] = temperatur

