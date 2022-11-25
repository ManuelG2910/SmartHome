from datenbank import datenbank
from datetime import datetime, timedelta

class infrarotheizung (datenbank):

    heizungAktivierung = 0
    heizungDeaktivierung = 0
    heizungPause = 0
    laufzeit = 0
    pruefungszeit = 0

    def __init__(self):
        super().__init__()

# Heizung wird aktiviert mit Maximum Laufzeit berechnung
    def heizung_aktivieren(self):

        # Zeit der Aktivierung speichern, nach 120 Minuten ausschalten
        heizungAktivierung = datetime.datetime.now()
        dt = datetime.strptime(heizungAktivierung, '%Y-%m-%d %H:%M:%S.%f')
        #heizungDeaktivierung = dt + timedelta(minutes= laufzeit)

# Heizung eird deaktiviert mit Pausenbechnung
    def heizung_deaktivieren(self):

        heizungDeaktivierung = datetime.datetime.now()
        dt = datetime.strptime(heizungDeaktivierung, '%Y-%m-%d %H:%M:%S.%f')
        #heizungPause = dt + timedelta(minutes=pruefungszeit)
        # die Zeit zurück auf 0 setzen

        heizungAktivierung = 0
        heizungDeaktivierung = 0

# Automatisiertes Heizen
    def heizung_automatisch(self):

        return True

# Prüfungszeiten anpassen
    def pruefungszeit_anpassen(pruefungszeit):

        pruefungszeit = pruefungszeit

# Laufzeit anpassen
    def laufzeit_anpassen(laufzeit):

        laufzeit = laufzeit

    # Update Tabelle Schwellenwert die Spalte Luftfeuchtigkeit
    def schwellwert_luftfeuchtigkeit_anpassen(self, luftfeuchtigkeit):

        mycursor = self._cnx.cursor()
        mycursor.execute("UPDATE Schwellenwert SET Temperatur ="+luftfeuchtigkeit)
        self._cnx.commit()


     # Update Tabelle Schwellenwert die Spalte Luftfeuchtigkeit
    def schwellwert_temperatur_anpassen(self, temperatur):

        mycursor = self._cnx.cursor()
        mycursor.execute("UPDATE Schwellenwert SET Temperatur =" +temperatur)
        self._cnx.commit()
