from param import Range

mes = int(input("Digite o um mes (1-12): "))
"""
if mes == 1:
    print("o mes 1 e Janeiro")
elif mes == 2:
    print("o mes 2 e Fevereiro")
elif mes == 3:
    print("o mes 3 e Março")
elif mes == 4:
    print("o mes 4 e Abril")
elif mes == 5:
    print("o mes 5 e Maio")
elif mes == 6:
    print("o mes 6 e Junho")
elif mes == 7:
    print("o mes 7 e Julho")
elif mes == 8:
    print("o mes 8 e Septembro")
elif mes == 9:
    print("o mes 9 e Oct")
elif mes == 10:
    print("o mes 10 e Novembro")
elif mes == 11:
    print("o mes 11 e Novembro")
elif mes == 12:
    print("o mes 12 e Dezembro")
else:
    print("Mes Invalido")

"""


match mes:
    case 1:
        print("o mes 1 e Janeiro")
    case 2:
        print("o mes 2 e Fevereiro")
    case 3:
        print("o mes 3 e Março")
    case _:
        print("Mes Invalido")




foo = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(foo[5:7])
print(Range(0,20) )