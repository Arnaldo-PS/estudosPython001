import PySimpleGUI as sg

class JogoDeAventura:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no lado Norte ou Sul do continente? (norte / sul)'
        self.pergunta2 = 'Você prefere a espada ou o escudo? (espada / escudo)'
        self.pergunta3 = 'Qual sua posição em uma batalha? (tatico / linha de frente)'
        self.final1 = 'Você foi um grande herói e será lembrado por todos!'
        self.final2 = 'Você foi um covarde e morreu de forma vergonhosa!'
        self.final3 = 'Você conseguiu virar o destino e ajudou o lado B a ganhar!!'
        self.final4 = 'Você lutou bravamente.. Mas não foi o suficiente e seu corpo foi jogado aos porcos..'


    def Iniciar(self):

        layout = [
            [sg.Output(size=(50,10),key='respostas')],
            [sg.Input(size=(50,10),key='escolha')],
            [sg.Button('Iniciar')],
            [sg.Button('Responder')]
        ]

        self.janela = sg.Window('Jogo de Aventura',layout)

        while True: 
            self.LerValores()
            if self.evento == sg.WIN_CLOSED:
                break
            elif self.evento == 'Iniciar':
                print(self.pergunta1)
                self.LerValores()
                if self.valores['escolha'] == 'norte':
                    print(self.pergunta2)
                    self.LerValores()
                    if self.valores['escolha'] == 'espada':
                        print(self.final1)
                    if self.valores['escolha'] == 'escudo':
                        print(self.final4)
            
                if self.valores['escolha'] == 'sul':
                    print(self.pergunta3)
                    self.LerValores()
                    if self.valores['escolha'] == 'tatico':
                        print(self.final2)
                    if self.valores['escolha'] == 'linha de frente':
                        print(self.final3)

    def LerValores(self):
        self.evento, self.valores = self.janela.Read()

jogo = JogoDeAventura()
jogo.Iniciar()
