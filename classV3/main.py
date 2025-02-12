from modelo import *

p = Pessoa('Nome', 'email', idade=40)

p2 = Pessoa('Nome', 'email', idade=16)



print(type(p2) is Pessoa)


if p > 18:
    print(f"o {p.nome} é maior de idade")
else:
    print(f"o {p.nome} é menor de idade")


print(p.idade)
p += 30
print(p.idade)


print(int(p))


print(p2.__dict__)
print(p2.__dir__())


dict = {'nome':'Ze carlos', 'email':'email', 'idade':40}

print(dict['nome'])