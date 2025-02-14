from modelos import *

al = Aluno("João", 15, "3A")
al2 = Aluno("Rui", 16, "3A")
p = Pessoa("Pedro", 20)
p2 = Pessoa("Ana", 40)

lst: list[Pessoa] = [al, al2, p, p2]

for i in lst:
    if isinstance(i, Aluno):
        print(i.turma)
    else:
        print("Nao e aluno")


al3 = al
print(al == al3)
print(al is al3)

print("-----" * 10)
al4 = Aluno("Rui", 16, "3A")
al2 = Aluno("Rui", 16, "3A")
print(al2 == al4)
print(al2 is al4)


