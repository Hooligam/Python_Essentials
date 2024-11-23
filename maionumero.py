"""
Nome: Jogo Random
Descrição: E uma atividade para fixar o aprendizado, referente a loops
Autor: Elias Assunção (Hooligam)
Version: 1.0.0

"""

lista = []
numero_maior = 0

for numero in range(10):
        numero = int(input("Digite um nuemro: "))
        lista.append(numero)

for numero in lista:
        if numero > numero_maior:
                numero_maior = numero


print(f"Voce informou a seguinte lista: {lista}")
print (f"O maior numero da sua lista e {numero_maior}")
