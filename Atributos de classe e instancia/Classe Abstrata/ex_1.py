from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractmethod
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
        return "LG"
    
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")
        
    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "Semp"
    
controle_tv = ControleTV()
controle_tv.ligar()
controle_tv.desligar()
print(controle_tv.marca)

print(f"\t")

controle_ar = ControleArCondicionado()
controle_ar.ligar()
controle_ar.desligar()
print(controle_ar.marca)