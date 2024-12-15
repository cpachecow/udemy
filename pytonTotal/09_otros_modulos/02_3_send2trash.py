import os
import send2trash
# Como send2trash no es una librería propia de Python, hay que instalarla.
# Se recomienda instalarla en un entorno virtual.
# Comando para su instalación es: pip install send2trash
# send2trash envía los archivos eliminados a la papelera
send2trash.send2trash('ejemplosTxt/02_ejemplo.txt')
