
class Escola:

    numero_alunos: int = 0

    def __init__(self, nome: str):
        self.__nome = nome
        self.turmas = []

    @classmethod
    def get_numero_alunos(cls):
        return cls.numero_alunos

    @staticmethod
    def get_numero_alunos_static():
        return Escola.numero_alunos


    @property
    def nome(self):
        return self.__nome


    @nome.setter
    def nome(self, nome):
        if nome == "":
            print("Nome não pode ser vazio")
            return

        self.__nome = nome

    @nome.deleter
    def nome(self):
        del self.__nome
        self.__nome = "nome pre-definido"
