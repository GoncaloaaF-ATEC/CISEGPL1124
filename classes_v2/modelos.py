from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    email: str

@dataclass
class Professor(Pessoa):
    pass


@dataclass
class Nota:
    ufcd: str
    nota: float
    professor: Professor
    aluno: "Aluno"


@dataclass
class Aluno(Pessoa):
    turma: str
    notas: list[Nota]

    def calcularMedia(self) -> float:

        total_nota = self.notas.__len__()
        sum = 0.0

        if total_nota > 0:
            for n in self.notas:
                sum += n.nota

            return sum / total_nota

        return None

    def add_notas(self, nota:Nota):
        nota.aluno = self
        self.notas.append(nota)


'''
p = Pessoa('Nome', 'email')

print(p)

a = Aluno('Nome', 'email', 'turma', [1, 2, 3])
print(a)

'''