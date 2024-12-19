def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar a funcao.")
        funcao(*args, **kwargs)
        print("Faz algo depois de executar a funcao.")
    
    return envelope

@meu_decorador # == hello_world = meu_decorador(hello_world)
def hello_world(nome, outro_args):
    print(f"Hello World {nome} !")


hello_world("Jorge", 1000)