"""
Nome: RPG Elias
Descrição: E uma atividade para fixar o aprendizado, referente a programação
orientada a objetos em python (Classes e Subclasses).
Autor: Elias Assunção (Hooligam)
Version: 1.0.0

"""

#  Classe base para criação de personagens
class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida    
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, botao):
        if botao == 'atacar':
            print('Atacando')
        elif botao == 'defender':
            print('Defendendo')

#   Subclasses de personagens
class Mago(Personagem):
    def __init__(self, nome): 
        super().__init__(nome=nome, vida=40, ataque=70, defesa=30)

class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=70, ataque=60, defesa=50)
        
class Assasino(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=55, ataque=80, defesa=20)
        


# teste para verificar se o programa esta funcionando.
personagem1 = Mago('Gandalf')
print(personagem1.nome)
personagem1.atacar('atacar')
personagem1.atacar('defender')