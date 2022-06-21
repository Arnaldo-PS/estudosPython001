import getpass

class Senha:
    def __init__(self):
        self.senha = getpass.getpass('Insira aqui sua senha: ')
        self.tent = 0

    def Iniciar(self):

        while True: 
            if getpass.getpass('Digite sua senha: ') == self.senha:
                print('Acesso liberado!')
                break
            else:
                self.tent = (self.tent + 1)
                if self.tent == 1:
                    print('2 tentativas restantes..')
                if self.tent == 2:
                    print('1 tentativa restante..')
                if self.tent == 3:
                    print('Acesso negado!')
                    break

trava = Senha()
trava.Iniciar()
