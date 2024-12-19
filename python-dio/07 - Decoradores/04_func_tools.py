import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        #funcao(*args, **kwargs)
        funcao(*args, **kwargs)
    
    return envelope

@meu_decorador # == hello_world = meu_decorador(hello_world)
def hello_world(nome, outro_args):
    print(f"Hello World {nome} !")


print(hello_world.__name__)