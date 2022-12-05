import pywhatkit
import os

from pywhatkit import sendwhatmsg_instantly, sendwhatmsg_to_group_instantly

hanynummer_liste = ["+4915730188009"]
gruppen_id = [""]


def nachricht_senden():
    for i in range(len(hanynummer_liste)):
        sendwhatmsg_instantly(
            phone_no=hanynummer_liste[i],
            message="Sturmwarnung",
            wait_time=15,
            tab_close=True,
            close_time=3
        )


def bild_senden():
    for i in range(len(hanynummer_liste)):
        pywhatkit.sendwhats_image(
            receiver=hanynummer_liste[i],
            img_path=os.path.join("..", "Bilder", "Sturmwarnung.png"),
            caption="Sturmwarnung!!",
            wait_time=15,
            tab_close=True,
            close_time=3
        )


def nachricht_gruppe_senden():
    sendwhatmsg_to_group_instantly(
        group_id="JlNQQrJxjgzKVJ34gPTegb",
        message="Hallo",
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
