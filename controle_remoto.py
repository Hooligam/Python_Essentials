"""
Nome: Controle Remoto
Descrição: E uma atividade para fixar o aprendizado, referente a programação
orientada a objetos em python.
Autor: Elias Assunção (Hooligam)
Version: 1.0.0

"""

class ControleRemoto:
    def __init__(self, cor, altura, largura):
        self.cor = cor
        self.altura = altura
        self.largura = largura
      
    def passar_canal(self, botao):
        if botao == 'up':
            print('Canal para cima')
        elif botao == 'down':
            print('Canal para baixo')

    def aumentar_volume(self, botao):
        if botao == 'mais':
            print('Volume para cima')
        elif botao == 'menos':
            print('Volume para baixo')    
    

# teste para verificar se o programa esta funcionando.

controle1 = ControleRemoto('preto', 10, 5)
print(controle1.cor)
controle1.passar_canal('up')


controle2 = ControleRemoto('branco', 15, 7)
print(controle2.cor)
controle2.aumentar_volume('mais')


