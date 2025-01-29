from dataclasses import dataclass

'''
class Morada:
    def __init__(self, cp1:int, cp2:int, porta:str, apt:str):
        self.cp1 = cp1
        self.cp2 = cp2
        self.porta = porta
        self.apt = apt
'''
@dataclass
class Morada:
    cp1: int
    cp2: int
    porta: str
    apt: str

    def getRua(self) -> str:
        return "Rua bla bla bla"



@dataclass
class Pessoa:
    nome: str
    idade: int
    morada: Morada

    def __init__(self, nome:str, idade:int, cp:str, porta:str, apt:str):
        self.nome = nome
        self.idade = idade
        self.cp = cp.split("-")
        m = Morada(int(cp[0]), int(cp[1]), porta, apt)
        self.morada = m

    def __str__(self):
        return f"Descrição da pessoa"

