"""
var ?
tuples ?
if/elif/else ?
match ?
for ?
while ?

def ?
class
  dunder methods
  herança


"""
from Escola import Escola

es = Escola("Escola 2")
es2 = Escola("Escola 2")

Escola.numero_alunos = 10

print(Escola.numero_alunos)

# print(es.numero_alunos) <- Evitar
# print(es2.numero_alunos) <- Evitar

print("---------------------")
print(Escola.get_numero_alunos())

print("-----------get_numero_alunos_static----------")
print(Escola.get_numero_alunos_static())
# print(es.get_numero_alunos_static()) <- Evitar


print("-----------@property----------")


print(es.nome)

es.nome = "Escola 3"

print(es.nome)
es.nome = ""



print("-----------@deleter----------")

print(es.__dir__())
del es.name
print(es.__dir__())