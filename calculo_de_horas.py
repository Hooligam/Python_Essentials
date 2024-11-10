print("Cadastre as horas das atividades do seu projeto!\n")

try:
    planejamaneto = int(input("Digite quantas horas voce gastou no planejamento do projeto? "))
    execucao = int(input("Digite quantas horas voce gastou executando as atividades previstas: "))
    impedimento = int(input("Digite quantas horas voce gastou resolvendo impedimento das atividades: "))
except: 
    print("Numero invalido, provavelmente voce digitou uma letra ou caracter invalido, tente novamente")
    exit()
if planejamaneto or execucao or impedimento <=0:
        print("Horas do seu projeto não podem ser apontadas de forma negativa")

total_de_horas = planejamaneto + execucao + impedimento

print(f"\nVoce gastou o total de {total_de_horas}hrs em seu projeto!")