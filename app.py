print('''

░░░▒█ ▒█▀▀▀█ ▒█▀▀█ ▒█▀▀▀█ 　 ▒█▀▀▄ ▒█▀▀▀█ 　 ▒█▄░▒█ ▒█░▒█ ▒█▀▄▀█ ▒█▀▀▀ ▒█▀▀█ ▒█▀▀▀█ 　 ▒█▀▀▀█ ▒█▀▀▀ ▒█▀▀█ ▒█▀▀█ ▒█▀▀▀ ▀▀█▀▀ ▒█▀▀▀█ 
░▄░▒█ ▒█░░▒█ ▒█░▄▄ ▒█░░▒█ 　 ▒█░▒█ ▒█░░▒█ 　 ▒█▒█▒█ ▒█░▒█ ▒█▒█▒█ ▒█▀▀▀ ▒█▄▄▀ ▒█░░▒█ 　 ░▀▀▀▄▄ ▒█▀▀▀ ▒█░░░ ▒█▄▄▀ ▒█▀▀▀ ░▒█░░ ▒█░░▒█ 
▒█▄▄█ ▒█▄▄▄█ ▒█▄▄█ ▒█▄▄▄█ 　 ▒█▄▄▀ ▒█▄▄▄█ 　 ▒█░░▀█ ░▀▄▄▀ ▒█░░▒█ ▒█▄▄▄ ▒█░▒█ ▒█▄▄▄█ 　 ▒█▄▄▄█ ▒█▄▄▄ ▒█▄▄█ ▒█░▒█ ▒█▄▄▄ ░▒█░░ ▒█▄▄▄█''')

import random

class Jogo_Do_Numero_Secreto:
    def __init__(self):
        print('\nEscolha um numero entre 1 e 10')
        self.numero_secreto = random.randint(1, 10)
        self.chute = 0 # Inicializa o chute com um valor padrão

    def verificar_chute(self):
        if self.numero_secreto > self.chute:
            return 'numero secreto é maior'
        elif self.numero_secreto < self.chute:
            return "numero secreto é menor"
        else:
            return 'Você acertou!'

jogo = Jogo_Do_Numero_Secreto()

while True:
    jogo.chute = int(input('Digite um número: '))
    resultado = jogo.verificar_chute()
    print(resultado)
    if resultado == 'Você acertou!':
        break