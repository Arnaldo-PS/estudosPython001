import PySimpleGUI as sg
from random import randint

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'),sg.Button('não')]
        ]
   
    def Iniciar(self):
        self.janela = sg.Window('Simulador de dado',layout=self.layout)
        self.eventos, self.valores = self.janela.Read()
          
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                        self.GerarValorDoDado()
            elif self.eventos == 'não' or self.eventos == 'n':
                        print('Obrigado por jogar!')
            else:
                        print('Favor digitar "sim" ou "não".')
        except:
            print('Ocorreu um erro ao receber sua resposta!')
        
    def GerarValorDoDado(self):
        print(randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()
