print("Vamos calcular o seu IMC\n")

try:
    peso = float(input("Me informe o seu peso atual: "))
    altura = float(input("Me informe a sua altura: "))
except:
    print("Favor iserir um numero valido, não utilize (,) ou letras. ")
    exit()

imc = peso / (altura ** 2)

if imc < 18.5: 
    print("\nVoce esta abaixo do peso ideal")
elif imc < 25:
    print("\nVoce esta dentro do peso ideal")
else:
    print ("Voce esta acima do peso, se cuide")

