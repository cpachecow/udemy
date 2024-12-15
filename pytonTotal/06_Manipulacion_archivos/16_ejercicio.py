from pathlib import Path

ruta = Path("America","Chile","La Serena","Valle del Elqui", "Cochiguaz")
#print(ruta)

# relative_to: Devuelve un objeto Path, con el argumento determinado. 
#              Entrega el contenido de un directorio especifico.

# Entrega ruta dentro de 'America'
en_america = ruta.relative_to(Path("America"))
print(en_america)

# Entrega ruta dentro de 'Chile'
en_chile = ruta.relative_to(Path("America","Chile"))
print(en_chile)