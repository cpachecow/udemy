def numero_perfumeria():
    num = 0
    const = "P"
    while True:        
        yield f"{const}-{num}"
        num +=1


def numero_farmacia():
    num = 0
    const = "F"
    while True:
        yield f"{const}-{num}"
        num +=1


def numero_cosmetica():
    num = 0
    const = "C"
    while True:
        yield f"{const}-{num}"
        num +=1


gen_perfumes = numero_perfumeria()
gen_farmacia = numero_farmacia()
gen_cosmetica = numero_cosmetica()
