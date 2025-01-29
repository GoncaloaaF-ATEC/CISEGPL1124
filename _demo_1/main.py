'''

var
print
input
type cast int("10")
if



'''


idade = int(input("idade: "))

print(idade)



print("Val 1", end="-")
print("Val 2")

print("--" * 3)

print("Val 2", "val 4", sep=" <-> ")

print("--" * 3)

v1 = 10
v2 = 20.3

print(v1 + v2)

print("--" * 3)


val = int(input("val: "))

print("Antes do if")
if val > 10:
    print("----inicio do bloco")

    print("----val maior que 10")

    print("----fim  do bloco")
else:
    print("----inicio do bloco")

    print("----val nenor ou igual a 10")

    print("----fim do bloco")


print("depois do if")



"""

Faça um porgrama que receba 2 num e mostre o maior


num1 = 10
num2 = 10

"""

num1 = int(input("num1: "))
num2 = int(input("num2: "))

if num1 > num2:
    print(f"o num maio é {num1}")
else:
    print(f"o num maio é {num2}")



"""

Faça um porgrama que receba 2 num e mostre o maior mas se forem igais indique que sao iguais

"""

if num1 > num2:
    print(f"o num maio é {num1}")
elif num2 > num1:
    print(f"o num maio é {num2}")
else:
    print(f"São iguais")

print("-----" * 3)


print("""    Ola Mundo
    Ola Mundo 2    """)
print("    Ola Mundo     ")

print("-----" * 3)
print("-----" * 3)


menu = """
--------Menu--------
| opt1---------- 1 |
| opt2---------- 2 |
| opt3---------- 3 |
| opt4---------- 4 |
--------------------
"""

"Comentatio"

# cmt

#TODO:
#FIXME:

print(menu)




"""

and
or

^ - xor -> T se apenas um dos lados for T
"""
print("--------------------")
b1 = True
b2 = True

print(b1 ^ b2)

print("--------------------")


num1 = int(input("num1: "))
num2 = int(input("num2: "))
num3 = int(input("num3: "))


if num1 > num2 and num1 > num3:
    print(f"o maior é o {num1}")

"""
num1  = 10
num2 = 50
num3 = 1
"""


if num1 > num2 or num1 > num3:
   print(f"o {num1} não e o menor")
