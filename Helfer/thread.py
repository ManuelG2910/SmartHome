from threading import Thread
from Hausautomations import sturmwarnung
from Hausautomations import infrarotheizung


thread_1 = Thread(target=sturmwarnung.schwellenwert_Strumwarnung_pruefen)
thread_2 = Thread(target=infrarotheizung.balkonkraftwerk_strom_pruefung)
thread_3 = Thread(target=infrarotheizung.laufzeit_pruefen)
thread_4 = Thread(target=infrarotheizung.optimiertes_Heizen)


thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
