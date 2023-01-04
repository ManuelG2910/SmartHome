from pywhatkit import whats
import os

hanynummer_liste = ["+4915730188009"]
gruppen_id = [""]
gruppen_id = "JlNQQrJxjgzKVJ34gPTegb"
nachricht = "Achtung, starker Wind! Ist alles Windsicher?"


def nachricht_senden():
    for i in range(len(hanynummer_liste)):
        whats.sendwhatmsg_instantly(
            phone_no=hanynummer_liste[i],
            message=nachricht,
            wait_time=15,
            tab_close=True,
            close_time=3
        )


def bild_senden():
    for i in range(len(hanynummer_liste)):
        whats.sendwhats_image(
            receiver=hanynummer_liste[i],
            img_path=os.path.join("..", "Bilder", "Sturmwarnung.png"),
            caption=nachricht,
            wait_time=15,
            tab_close=True,
            close_time=3
        )


def nachricht_gruppe_senden():
    whats.sendwhatmsg_to_group_instantly(
        group_id=gruppen_id,
        message=nachricht,
        wait_time=15,
        tab_close=True,
        close_time=3
    )


# Neue Mobilnummer zu Dictionary hinzufügen
def mobilnummer_hinzufuegen(mobilnummer):
    hanynummer_liste.append(mobilnummer)


# Vorhandene Mobilnummer in Dictionary anpassen
def mobilnummer_aendern(mobilnummer_alt, mobilnummer_neu):
    hanynummer_liste.remove(mobilnummer_alt)
    hanynummer_liste.append(mobilnummer_neu)


# Vorhandene Mobilnummer löschen
def mobilnummer_loeschen(mobilnummer):
    hanynummer_liste.remove(mobilnummer)


def guppen_id_aendern(grupen_id_neu):
    gruppen_id=grupen_id_neu


def nachricht_aendern(nachricht_neu):
     nachricht = nachricht_neu
