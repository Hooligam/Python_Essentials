"""
Nome: Clientes no aplicativo de streming
Descrição: E uma atividade para fixar o aprendizado, referente a programação
orientada a objetos em python.
Autor: Elias Assunção (Hooligam)
Version: 1.0.0

"""

#criar usuario, planos, produto.

class Cliente:
    def __init__(self, nome, email,):
        self.nome = nome
        self.email = email
        self.plano = "Basico"
    

    def mostrar_dados(self):
        print(f'Nome: {self.nome}\nEmail: {self.email}\nPlano: {self.plano}')

    def mudar_plano(self, novo_plano):
        if self.plano == "Basico":
            self.plano = "Premium"
        else:
            self.plano = "Basico"
        print(f'Plano alterado para: {self.plano}')

    def assistir_filme(self, nome_filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Assistindo filme: {nome_filme}')
        elif self.plano == "Premium":
                print(f'Assistindo filme: {nome_filme}')
        else:
            print('Plano não permite assistir esse filme, faça um upgrade para assistir')



Cliente1 = Cliente('Elias Assunção', 'eliasassuncao10000@gmail.com')
Cliente1.mostrar_dados()
print("\n")
# Usuario clica para assistir um filme que não esta no plano dele
print("Carregando filme selecionado ...")
Cliente1.assistir_filme("Vingadores", "Premium")
print("\n")

# usuario tenta assistir um filme compativel com seu plano basic
print("Alterando o filme selecionado ...")
Cliente1.assistir_filme("A bela e a Fera", "Basico")
print("\n")

# usuario muda de plano
Cliente1.mudar_plano("Premium")

# usuario tenta assistir um filme compativel com seu novo plano
Cliente1.assistir_filme("Vingadores", "Premium")