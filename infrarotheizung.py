from datenbank import datenbank
from datetime import datetime, timedelta

class infrarotheizung (datenbank):

    heizungAktivierung = 0
    heizungDeaktivierung = 0
    heizungPause = datetime(0)
    laufzeit = 0
    pruefungszeit = 0

    def __init__(self):
        super().__init__()

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
    def heizung_automatisch(self):

        return True

# Prüfungszeiten anpassen
    def pruefungszeit_anpassen(pruefungszeit):

        pruefungszeit = float(pruefungszeit)

# Laufzeit anpassen
    def laufzeit_anpassen(laufzeit):

        laufzeit = float(laufzeit)

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
