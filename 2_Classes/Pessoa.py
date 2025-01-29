class Pessoa:

    def __init__(self, nome, idade, peso = 50.0):
        self.nome = nome
        self.idade = idade
        self.peso = peso


    def engordar(self, engorda):
        if engorda > 0:
            self.peso += engorda
        else:
            print("Peso Invalido")




p1 = Pessoa("Rui", 21)
p2 = Pessoa("Jose", 25)

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)

print("--------------")

print(p1.peso)
print(p2.peso)

p1.engordar(20)

print(p1.peso)
print(p2.peso)

p1.engordar(-20)
print(p1.peso)



print("----------------")

p1 = Pessoa("Rui", 21)
p2 = Pessoa("Jose", 25, 30.0)

print(p1.peso)
print(p2.peso)

p2.engordar(90)

print(p2.peso)



class hero:
    def __init__(self, nome, cls, maxPower, maxHP = 100):
        self.nome = nome
        self.cls = cls
        self.maxHP = maxHP
        self.maxPower = maxPower
        self.active_armor = None
        self.armor = []
        self.itens = []



"""

Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor



Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;


"""