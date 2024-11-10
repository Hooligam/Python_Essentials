print("Verificar temperatura para integridade do servidor\n")

try:
    temperatura = int(input("Informe a temperatura em que se incontra a sala do servidor: "))
except:
    print("Digite apenas o valor da temperatura, sem simbolos ou letras")
    exit()
if temperatura < 30:
    print("Temperatura em estado normal")
else:
    print("CUIDADOOO SERVIDOR PODE SER DANIFICADO PELA ALTA TEMPERATURA")
