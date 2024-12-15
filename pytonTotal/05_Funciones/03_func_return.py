# Return dentro de las funciones, devueve el valor que se requiera.
#  a diferencia del print, este valor queda en el código, el print no.

def mult(num1, num2):
    return (num1 * num2)

resultado = mult(2,8)
print(resultado)

def potencia(num1, num2):
    return num1 ** num2

resultado = potencia(8,2)
print(resultado)

def usd_a_eur(usd):
    return usd * 0.9

usd = 20
euro = usd_a_eur(usd)
print(f'{usd} dolares equivalen a {euro} euros')

# Crea una función llamada invertir_palabra que tome los caracteres de una palabra dada como argumento,
#  invierta el orden de sus caracteres y los devuelva de ese modo y en mayúsculas.
#  Por ejemplo, si le proporcionamos la palabra "Python", deberá devolver: "NOHTYP"
def invertir_palabra(texto):
    t = texto[::-1].upper()
    return t

texto_inv = invertir_palabra('Estoy programando!')
print(texto_inv)

