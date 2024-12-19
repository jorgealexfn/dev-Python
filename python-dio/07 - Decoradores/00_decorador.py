def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar a funcao.")
        funcao()
        print("Faz algo depois de executar a funcao.")
    
    return envelope

@meu_decorador # == hello_world = meu_decorador(hello_world)
def hello_world():
    print("Hello World!")


hello_world()