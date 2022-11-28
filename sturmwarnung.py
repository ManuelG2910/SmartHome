from datenbank import datenbank


class sturmwarnung(datenbank):


    def __init__(self):
        super().__init__()

    # Insert into Sturmwarnung VALUES(mobilnummer, standardtext)
    def mobilnummer_hinzufuegen(mobilnummer, self):

        mycursor = self._cnx.cursor()
        mycursor.execute("INSERT INTO Sturmwarnung VALUES("+mobilnummer+",'Sturmwarnung')")
        self._cnx.commit()

    # UPDATE Sturmwarnung set mobilnummer = ? where mobilnummer = ?
    def mobilnummer_aendern(self):

        mycursor = self._cnx.cursor()
        mycursor.execute("UPDATE Sturmwarnung set mobilnummer where mobilnummer')")
        self._cnx.commit()

    # DELETE FROM Sturmwarnung
    def mobilnummer_loeschen(self):
        mycursor = self._cnx.cursor()
        mycursor.execute("DELETE Sturmwarnung  where mobilnummer")
        self._cnx.commit()

#def schwellenwert_Strumwarnung_aendern(self):
#def schwellenwert_Strumwarnung_pruefen(windwert, self):""
#def nachricht_senden(self):
