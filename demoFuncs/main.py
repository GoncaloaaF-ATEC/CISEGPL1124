def ola_Mundo(nome:str,aplido:str, idade:int = 20, ano:int = 2024) -> str:
    return f"Olá, mundo!, {nome} {aplido}, {idade} no ano {ano}"



print(ola_Mundo('Joao', "Paulo" , 40, 2055))

print(ola_Mundo('Joao', "Paulo" , ano=3000))