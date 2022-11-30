class sturmwarnung:

    def __init__(self):
        self.anzahl_Mobilnummer = 0

        self.thisdict = {
            "Schwellenert_Strumwarnung": 3.0,
            "Nachricht Sturmwarnung": "Achtung, starker Wind! Ist alles sicher?"
        }

    # Neue Mobilnummer zu Dictionary hinzufügen
    def mobilnummer_hinzufuegen(mobilnummer, self):
        anzahl_Mobilnummer =+1
        thisdict["Handynummer" + str(anzahl_Mobilnummer)] = mobilnummer

    # Vorhandene Mobilnummer in Dictionary anpassen
    def mobilnummer_aendern(mobilnummer_alt, mobilnummer_neu, self):
        key = thisdict.values(mobilnummer_alt)
        thisdict[key] = mobilnummer_neu

    # Vorhandene Mobilnummer löschen
    def mobilnummer_loeschen(mobilnummer, self):
        key = thisdict.values(mobilnummer)
        del thisdict[key]

    # Stellenwert in Dictionary anpassen
    def schwellenwert_Strumwarnung_aendern( schwellenwert_Sturm,self):
        thisdict["Schwellenert_Strumwarnung"] = schwellenwert_Sturm

    # aktueller Windwert wird mit dem Stellenwert abgeglichen und ggf wird eine Nahcricht versendet
    def schwellenwert_Strumwarnung_pruefen(windwert, self):
        if thisdict["Schwellenert_Strumwarnung"] >= windwert:
            print("Sturmwarnung")
            nachricht_senden(windwert)

    # Nachricht wird bei Sturmwarnung versendet
    def nachricht_senden(windwert, self):
        '''
                Code
                '''
