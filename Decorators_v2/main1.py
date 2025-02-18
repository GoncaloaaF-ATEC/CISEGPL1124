def calcMediaNotas(*args):
    sum = 0
    for i in args:
        sum += i
    return sum / len(args)


print(calcMediaNotas(10, 8, 9, 7, 6))

# print(calcMediaNotas([10, 8, 9, 7, 6]))


def calcMediaNotas(**bla_bla_bla):
    print(bla_bla_bla)


calcMediaNotas(nome='João', idade=20, cidade='Lisboa')

def ola(nome: str) -> str:
    return f'Olá {nome}'

print(ola('João'))
print(ola(nome="João"))


def demo(*args, **kwargs):
    print(args)
    print(kwargs)


demo(1, 2, 3, nome='João', idade=20, cidade='Lisboa')