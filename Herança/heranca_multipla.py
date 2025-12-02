class Animal:
    def __init__(self, num_patas):
            self.num_patas = num_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}'
         for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
     def __init__(self, cor_pelo, **kw):
            self.cor_pelo = cor_pelo
            #Chamando o construtor pai.
            super().__init__(**kw)

class Ave(Animal):
   def __init__(self, cor_bico, **kw):
            self.cor_bico = cor_bico
            #Chamando o construtor pai.
            super().__init__(**kw)

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Orinitorinco(Mamifero,Ave):
    pass

gato_1 = Gato(num_patas = 4, cor_pelo = "Preto")
print(gato_1)

# Ao utilizar kwargs é necessario utilizar chave e valor.
ornitoorinco_1 = Orinitorinco(num_patas = 4, cor_pelo = "cinza", cor_bico = "laranja" )
print(ornitoorinco_1)