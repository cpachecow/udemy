# En Python se pueden crear Módulos y Paquetes propios.

# Deficiones

# 1.- Módulos: Son todos los archivos '.py' que pueden contener 
#              variables, funciones, clases, importacion de otros paquetes, entre otros.
#
# 2.- Paquetes: Es la agrupación de Módulos en carpetas, para que Python pueda reconocer
#               una carpeta como un paquete debe tener el archivo '__init__py'; para
#               luego tener sus modulos y sub Paquetes, que también deben tener el archivo
#               anteriormente mencionado.

# Sintaxis para importar un módulo llamado 'funciones.py'

import funciones

funciones.llorar()

# Sintaxis para importar una funcion específica del módulo funciones.py

from funciones import sonreir

sonreir()


# Sintaxis para importar desde un paquete un módulo

from MiPaquete import mimodulo

mimodulo.despedida()


# Sintaxis para importar desde un subpaquete un módulo

from MiPaquete.MISubPaquete import frases

frases.fraseUno()