numero = int(input("Digite um numero entre 0 a 9999: "))
u = numero // 1 % 10
d = numero // 10 % 100
c = numero // 100 % 1000
um = numero // 1000
print(f'unidades: {u}')
print(f'dezenas: {d}')
print(f'centenas: {c}')
print(f'unidades de milhar: {um}')