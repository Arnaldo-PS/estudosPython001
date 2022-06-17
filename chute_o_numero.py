import PySimpleGUI as sg
from random import randint

from pygame import WINDOWCLOSE

class ChuteONumero:
    def __init__(self):
        self.valorAleatorio = 0
        self.valorMinimo = 1
        self.valorMaximo = 99
        self.tentarNovamente = True
    
    def Iniciar(self):

        # utilizando PySimpleGUI
        # add layout
        layout = [
            [sg.Text('Seu chute',size=(39,0))],
            [sg.Input(size=(18,0),key='valorChute')],
            [sg.Button('Chutar'),sg.Button('Fechar')],
            [sg.Output(size=(20,10))]
        ]

        # add janela
        self.janela = sg.Window('Chute o numero!',layout=layout)
        self.GerarValorAleatorio()

        try:
            while True:
                # add valores
                self.evento, self.valores = self.janela.Read()
                if self.evento == sg.WIN_CLOSED or self.evento == 'Fechar':
                    break
                elif self.evento == 'Chutar':
                    self.valorChute = self.valores['valorChute']
                    while self.tentarNovamente == True:
                        if int(self.valorChute) > self.valorAleatorio:
                            print('Chute um valor menor!')
                            break
                        elif int(self.valorChute) < self.valorAleatorio:
                            print('Chute um valor maior!')
                            break
                        else:
                            self.tentarNovamente == False
                            print('Parabéns você acertou!')
                            break 
                        
        except:
            print('Favor digitar apenas números..')
            self.Iniciar()
    
    def GerarValorAleatorio(self):
        self.valorAleatorio = randint(self.valorMinimo, self.valorMaximo)

chute = ChuteONumero()
chute.Iniciar()
