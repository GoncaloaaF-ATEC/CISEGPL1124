def msg2(func):
    def wrapper(self, *args, **kwargs):
        print("Hello")
        func(self, *args, **kwargs)
        print("World")

    return wrapper



class My_Class:
    def __init__(self):
        self.name = "My_Class"


    @msg2
    def print_name(self, name:str, idade:int=20):
        print(self.name)



obj = My_Class()
obj.print_name("Carlos", idade=20)