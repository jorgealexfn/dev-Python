class myIteretor:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador] 
            self.contador += 1
            return numero * 2
            # raise StopIteration
        except IndexError:
            raise StopIteration

for i in myIteretor(numeros=[38, 13, 11]):
    print(i)
    