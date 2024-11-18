"""
Nome: Exercicio idades
Descrição: E uma atividade para fixar o aprendizado, referente a condiçoes no python
Autor: Elias Assunção (Hooligam)
Version: 1.0.0

"""
# Parte inicial e coleta dos dados

print("Bem vindo ao nosso programa que descobre se voce é uma Criança, Adolescente, Adulto ou um Idoso\n")
nome = input("Me informe, seu nome: ")

try:
    idade = int(input(f"Certo {nome}, me informe quantos anos voce tem? "))

# Logica que ira determinar baseado na idade a qual categoria a pessoa se encaixa

    if idade <= 12:
        print(f"Apos a nossa analise {nome}, verifiquei que voce e uma criança")
    elif idade > 12 and idade <= 17:
        print(f"Apos a nossa analise {nome}, verifiquei que voce e um Aborrecente asudhasu")
    elif idade > 17 and idade <= 64:
        print(f"Apos a nossa analise {nome}, verifiquei que voce e um Adulto")
    else:
        print(f"Apos a nossa analise {nome}, verifiquei que voce e um Idoso")
except: 
    print(f"Ops, {nome}, parece que você digitou algo que não é um número. Tente novamente e insira apenas números para sua idade.")