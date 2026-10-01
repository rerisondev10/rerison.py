aluno = {}
aluno["nome"] = str(input("Qual o seu nome: "))
aluno["media"] = float(input("Qual sua média: "))
print(f'Olá {aluno["nome"]} sua média foi {aluno["media"]}')

if aluno["media"] >= 6 and aluno["media"] <=10:
    print(f'{aluno["nome"]} você foi aprovado')
elif aluno["media"] >10:
    print(f'{aluno["nome"]}, a nota não pode passar de 10.')
else:
    print(f'{aluno["nome"]} você foi reprovado, infelizmente. Estude um pouco mais.')
