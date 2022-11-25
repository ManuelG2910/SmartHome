import mysql.connector

# Datenbankverbindung
class datenbank:

    def __init__(self):
        self._cnx = None

# Datenbankverbindung wird hergestellt
    def __enter__(self):
        self._cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mysmarthome")

# Datenbankverbindung wird geschlossen
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cnx.close()
