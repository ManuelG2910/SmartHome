from threading import Thread
from Hausautomations import sturmwarnung
from Hausautomations import infrarotheizung
from Hausautomations import warmwasserboiler
"""
 es werden Threads benötigt, da bestimmte Methoden regelmäßig überprüft werden müssen
 --> in den Methoden ist eine dauerschleife, die schlafen geschickt wird
"""

# Threads werden erzeugt und werden mit der für sie vorgesehenen Methode verknüpft
thread_1 = Thread(target=sturmwarnung.schwellenwert_Strumwarnung_pruefen)
thread_2 = Thread(target=infrarotheizung.balkonkraftwerk_strom_pruefung)
thread_3 = Thread(target=infrarotheizung.laufzeit_pruefen)
thread_4 = Thread(target=infrarotheizung.optimiertes_Heizen)
thread_5 = Thread(target=warmwasserboiler.automatik)
thread_6 = Thread(target=warmwasserboiler.fall_4_Solar)

# Threads werden gestartet
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_5.start()
thread_6.start()
