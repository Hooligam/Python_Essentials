"""
Nome: Jogo Random
Descrição: E uma atividade para fixar o aprendizado, referente a loops
Autor: Elias Assunção (Hooligam)
Version: 1.0.0

"""
import random

numero = random.randint(1,100)
tentativa = 0


print("Vamos jogar um jogo de adivinhação?\n")
print("Escolha um numero de 1 a 100\n")

while True:
    tentativa += 1
    try:
        numero_escolhido = int(input("Digite o numero escolhido: "))
        if numero_escolhido == numero:
            print(f"Parabens, voce acertou o numero em {tentativa} tentativas")
            break
        elif numero_escolhido > numero:
            print ("tente um numero menor")
        else:
            print ("tente um numero maior")

        if tentativa == 15:
            print(f"Infelizmente, o numero correto era {numero}")
            break
    except:
        print("Favor digitar um numero valido")