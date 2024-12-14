class Animal:
    def __init__(self, nro_patas):
        self.nro_patas * nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {' . '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
        super().__init__(nro_patas)

class Ave(Animal):
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
        super().__init__(nro_patas)

class Ornitorrinco(Mamifero, Ave):
    pass

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

gato = Gato(4)
print(gato)
