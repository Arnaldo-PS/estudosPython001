from random import randint

class ChuteONumero:
    def __init__(self):
        self.valorAleatorio = 0
        self.valorMinimo = 1
        self.valorMaximo = 99
        self.tentarNovamente = True
    
    def Iniciar(self):
        self.GerarNumero()
        self.PedirValorAleatorio()
        
        try:
            while self.tentarNovamente == True:
                if int(self.valorChute) > self.valorAleatorio:
                    print('Chute um valor menor!')
                    self.PedirValorAleatorio()
                elif int(self.valorChute) < self.valorAleatorio:
                    print('Chute um valor maior!')
                    self.PedirValorAleatorio()
                else:
                    self.tentarNovamente == False
                    print('Parabéns você acertou!')
                    break
        except:
            print('Favor digitar apenas números..')
            self.Iniciar()
    
    def PedirValorAleatorio(self):
        self.valorChute = input('Chute um número: ')
    
    def GerarNumero(self):
        self.valorAleatorio = randint(self.valorMinimo, self.valorMaximo)

chute = ChuteONumero()
chute.Iniciar()
