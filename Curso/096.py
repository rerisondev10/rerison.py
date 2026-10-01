def area():
    largura = float(input("Qual a largura do seu terreno ? "))
    comprimento = float(input("Qual o comprimento do seu terreno ? "))
    conta = largura * comprimento
    return conta

resultado = area()
print(f"A área do seu terreno é: {resultado}")