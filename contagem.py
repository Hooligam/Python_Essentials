"""
Nome: Soma e repetição
Descrição: E uma atividade para fixar o aprendizado, referente a loops
Autor: Elias Assunção (Hooligam)
Version: 1.0.0

"""

print("Bem vindo! Esse programa mostra a soma dos numeros digitados no terminal")
print("quando quiser parar de somar os numeros, basta digitar 0\n")

soma = 0
contador = 0
while True:
    try:
        numero = int(input("Digite um nuemro: "))
        if numero == 0:
            break
        soma += numero
        contador += 1
    except:
        print("Favor digitar um numero valido")
    
media = soma / contador

print(f"O valor da soma dos numeros digitados e igual a {soma} ")
print(f"A quantidade de numeros digitados foram {contador}")
print(f"A media dos numeros e {media:,.2}")
