import random
usuario= int(input("Digite um numero inteiro de 0 a 5: "))
numero_escolhido_pelo_comput= random.randint(0,5)
if usuario == numero_escolhido_pelo_comput:
    print("Você acertou !")
else:
    print("você errou !")
print(f"O numero escolhido pelo computador foi: {numero_escolhido_pelo_comput}")

