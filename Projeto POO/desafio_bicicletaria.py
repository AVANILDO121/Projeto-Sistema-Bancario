class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("PIPIPIPI")
    
    def parar(self):
        print("Parando.....")
        print("Bicicleta parada.")
    
    def correr(self):
        print("Vrummm...")
    
    # Fazendo representação de classe.
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}'
         for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("Vermelha", "Soft", 2024, "R$ 999") 

# Chamando metodo.
b1.buzinar()
b1.correr()
b1.parar()

# Pedindo para exibir os atributos da classe.
print(f"Minha bike é {b1.cor}, o modelo é {b1.modelo}, ela é de {b1.ano}, e custou {b1.valor}.")

# Chamando a representação de classe
print(b1)