from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int

    def __func_pessoa(self):
        print("func pessoa")

    def func_comum(self):
       return "func comum pessoa"

    def __str__(self):
        return f"{self.nome} tem {self.idade} anos"


@dataclass
class Aluno(Pessoa):
    turma:str

    def __func_aluno(self):
        print("func Aluno")

    def func_comum(self):
        return "func comum Aluno"

    def __str__(self):
        return f"{self.nome} tem {self.idade} anos e está na turma {self.turma}"
