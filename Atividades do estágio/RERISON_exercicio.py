#Calcular subtotal, desconto e total, recusando valores negativos

subtotal = float(input("Qual o valor do produto ? "))
if subtotal <= 0:
    print("O subtotal não pode ser negativo !")
else:
    print("O Produto terá um desconto")

desconto = int(input("Qual o desconto desejado ? "))
tranformando_desconto = desconto /100
valor_desconto = subtotal * tranformando_desconto

if desconto > 50:
    print("Desconto não permitido")
else:
    print(f"O valor total é: {subtotal-valor_desconto}")
