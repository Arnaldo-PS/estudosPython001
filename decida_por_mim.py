import PySimpleGUI as sg
from random import choice

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

        layout = [
            [sg.Text('Faça sua pergunta:')],
            [sg.Input()],
            [sg.Output(size=(20,10))],
            [sg.Button('Decida por mim')]
        ]

        self.janela = sg.Window('Decida por mim',layout)       
        
        while True:

            self.evento, self.valores = self.janela.Read()

            if self.evento == sg.WIN_CLOSED:
                break
            elif self.evento == 'Decida por mim':
                print(choice(self.respostas))
        

decida = DecidaPorMim()
decida.Iniciar()
