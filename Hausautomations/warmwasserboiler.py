from datetime import datetime, timedelta

# Default-Wert = aus
aktivierungszeit= None
statusaktiv = "aus"
startzeit = datetime.now()
endzeit = datetime.now()
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




automatik(startzeit, endzeit)


#    def pruefungszeit_anapssen(self):


   # def tarifzeiten_anpassen(self):


 #   def laufzeit_anpassen(self):


 #   def solarstromwerte_anpassen(self):


