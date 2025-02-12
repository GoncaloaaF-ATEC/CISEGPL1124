
class Pessoa:

    def __init__(self, nome:str, email:str, idade:int = 20):
        self.nome = nome
        self.email = email
        self.idade = idade


    def __str__(self):
        return f"Nome: {self.nome}, Email: {self.email}"


    def __ge__(self, other):
        return self.idade >= other.idade

    def __gt__(self, other):
        if type(other) is Pessoa:
            return self.idade > other.idade

        elif type(other) is int:
            return self.idade > other

        return False

    def __add__(self, other):
        if type(other) is int:
            self.idade += other

        return self

    def __sub__(self, other):
        if type(other) is int:
            self.idade -= other

        return self

    def __int__(self):
        return self.idade