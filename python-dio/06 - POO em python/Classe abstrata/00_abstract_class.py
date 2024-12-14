from abc import ABC, abstractmethod, abstractproperty, property
#criando o modulo com a extensão


class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        #metodos
        pass
    
    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligado!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligado!")
    
    @property
    def marca(self):
        return "Samsumg"

class ControleDeArcondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o ar-Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o ar-Condicionado...")
        print("Desligado!")
    
    @property
    def marca(self):
        return "Samsumg"

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleDeArcondicionado()
controle.ligar()
print(controle.marca)
