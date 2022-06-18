import PySimpleGUI as sg
import random

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso!',
            'Não sei, você é quem sabe..',
            'Não faça isso!',
            'Acho que está na hora certa!',
            'Sim', 'Não'
        ]

    def Iniciar(self):
        input('Faça sua pergunta: ')
        print(random.choice(self.respostas))


decida = DecidaPorMim()
decida.Iniciar()
