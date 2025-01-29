from modelos import Pessoa, Morada


#p = Pessoa("Gonçalo", 23, Morada(2342,134,"1", "3F"))


cp = "1231-231"

print(cp[4])

data = cp.split(cp[4])

print(data)
print(data[0])
print(data[1])


"""
1231-231 - split -
['1231', '231']

12312231 split 2
['1', '31', '', '31']
"""


p = Pessoa("Gonçalo", 23, "2342-134","1", "3F")

print(p)


"""

Crie uma Agenda de contactos 

funcionalidades:

Adicionar Contacto 
Listar todos os conactos 


é Orbigatorio usar class

"""