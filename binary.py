def binario(decimal):
    binario = ""
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

numero = int(input("Intruduce el número que quieres convertir a binario: "))
print(binario(numero))