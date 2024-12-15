# Herencia: Es cuando una clase hija hereda atributos y médotos de una clase padre.
#           Sirve cuando clases se parecen entre si, pero cada una tienen ciertas particularidades.
# 
#  Las clases y la herencia ayudan a no repetir código de forma innecesaria, dado que entre más código 
#  repetido, más dificulta su futura modificación. Esto viene del concepto DRY (Don't repeat yourself).

class Animal:
    pass

class Pajaro(Animal):
    pass

# Para saber de qué clase está heredando su clase hija, utilizo el método '__bases__').
print(Pajaro.__bases__)

# Para ver qué clase(s) hijas han sido heredadas de la clase padre, utilizo el método '__subclasses()__').
print(Animal.__subclasses__())