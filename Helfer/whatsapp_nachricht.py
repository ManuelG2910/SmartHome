import pywhatkit
import time
import os

phnone_number = "+4915730188009"
# def nachricht_senden(nummer, nachricht):
pywhatkit.sendwhatmsg(
    phone_no=phnone_number,
    message="Sturmwarnung!!",
    time_hour=12,
    time_min=39,
    wait_time=15,
    tab_close=True,
    close_time=5
)
time.sleep(10)
pywhatkit.sendwhats_image(
    receiver=phnone_number,
    img_path=os.path.join("..", "Bilder", "Sturmwarnung.png"),
    caption="Sturmwarnung!!",
    wait_time=15,
    tab_close=True,
    close_time=3
)
