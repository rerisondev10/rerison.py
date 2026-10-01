velocidade_carro= int(input("Qual a velocidade do carro ? "))
print(f"A velociade é {velocidade_carro}")
if velocidade_carro > 80:
    print("você foi multado !")
    print("O valor da multa foi de ")
else:
    print("você seguiu as normas de trânsito")