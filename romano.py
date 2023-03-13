def convertir_a_romano(num):
    valores = [("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100),
               ("XC", 90), ("L", 50), ("XL", 40), ("X", 10), ("IX", 9),
               ("V", 5), ("IV", 4), ("I", 1)]
    resultado = ""
    for romano, valor in valores:
        while num >= valor:
            resultado += romano
            num -= valor
    return resultado

for x in range(7000):
    print(convertir_a_romano(x+1))