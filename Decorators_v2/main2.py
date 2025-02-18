def msg(func):
    def inside():
        print("Start")
        func()
        print("End")

    return inside

@msg
def fn1():
    print('fn1')


@msg
def fn2():
    print('fn2')


@msg
def fn3():
    print('fn3')

print("----")
fn1()
print("----")
fn2()
print("----")
fn3()
print("----")