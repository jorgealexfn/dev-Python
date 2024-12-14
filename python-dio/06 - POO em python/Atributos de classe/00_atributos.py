class Estudante:
    escola = "Dio"

    def __init__(self, nome, matricula):
        self.nome = nome 
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
aluno_1 = Estudante("Jorge", 1)
aluno_2 = Estudante("Thamyres", 2)

print(aluno_1)
print(aluno_2)
