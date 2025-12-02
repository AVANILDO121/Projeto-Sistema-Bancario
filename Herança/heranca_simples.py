class Veiculo:
    # Atributos da classe pai.
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    # Definindo um metodo.
    def ligar_motor(self):
        print("Ligando o motor...")
        print("Motor ligado.")
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}'
         for chave, valor in self.__dict__.items()])}"
    

# Classe filho(Motocicleta) herdando Caracteristicas da classe pai(veiculo).
class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def carga(self):
        print("Sem carga")

moto_1 = Motocicleta("Preta","DGN-1424", 2)
moto_1.ligar_motor()

carro_1 = Carro("Vermelho", "RTY-2456", 4)
carro_1.ligar_motor()

caminhao_1 = Caminhao("Azul", "DHV-3638", 8)
caminhao_1.ligar_motor()
caminhao_1.carga()
