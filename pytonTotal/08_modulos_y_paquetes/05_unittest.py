'''
Unittest es una biblioteca de Python que nos permite probar nuestro código está funcionando
según lo esperado.

Su funcionamiento en simples palabras es:

1.- Un módulo a probar, ejemplo cambia_texto.py

2.- Otro módulo para hacer las pruebas.
    2.1.- Para realizar las pruebas debo importar la biblioteca 'unittest' y el módulo a probar.
    2.2.- Debo crear una clase que herede 'unittest.TestCase'
    2.3.- Cada método de prueba debe iniciar con la palabra 'test' para que realice las pruebas.
    2.4.- Inlcuir el método self.assertEqual, que recibe dos argumentos. El primero sobre lo que
          se requiere probar (médotodo por ejemeplo) y segundo con respecto al archivo que creo
          que debería devolver el método.
    2.5.- Incluir fuera de la clase lo siguiente:
           if __name__ == '__main__':
               unittest.main()

'''
import unittest
import cambia_texto


class ProbarCambiaTexto(unittest.TestCase):

    # Lós métodos de pruebas deben iniciar con la pabla 'test', para que funcione.
    def test_mayusculas(self):
        palabra = 'buenos días'
        resultado = cambia_texto.todo_mayusculas(palabra)
        # El siguiente médoto debe contener la funcion a probar (guardado en la variable resultado)
        # y cómo creo que será el resultado de la salida de la función.
        # self.assertEqual(resultado, 'BUENOS DÍAS')
        self.assertEqual(resultado, 'Buenos días')

# Sirve para saber qué función debe ejecutar, al iniciar el programa
if __name__ == '__main__':
    unittest.main()