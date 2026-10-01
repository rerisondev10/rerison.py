nome_completo= str(input('Qual seu nome completo ? '))
print(f"Seu nome em maiusculas é: {nome_completo.upper()}")
print(f"Seu nome em minusculas é: {nome_completo.lower()}")
print(f'Seu nome tem {len(nome_completo) - nome_completo.count(" ")} sem contar os espaços')
print(f'O nome {len(nome_completo.split()[0])} letras no primeiro nome')


