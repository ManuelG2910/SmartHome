from datetime import datetime, timedelta

# Default-Wert = aus
aktivierungszeit= None
statusaktiv = "aus"

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

aktuelle_Zeit = datetime. datetime.now()
dt = datetime.strptime(aktuelle_Zeit, '%Y-%m-%d %H:%M:%S.%f')
endzeit = dt+timedelta(minutes=float(thisdict["Laufzeit"]))

automatik(aktuelle_Zeit, endzeit)


#    def pruefungszeit_anapssen(self):


   # def tarifzeiten_anpassen(self):


 #   def laufzeit_anpassen(self):


 #   def solarstromwerte_anpassen(self):


