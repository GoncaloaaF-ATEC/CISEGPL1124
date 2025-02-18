def msg(func):
    def inside(*args, **kwargs):
        print("Start")
        func(*args, **kwargs)
        print("End")

    return inside

@msg
def fn1(nome:str):
    print(f'fn1 : {nome}')



fn1('João')