"""

r
w
a
x

----
t
b


"""


f = open('arquivo.txt', 'r')
#f.write('linha 1\n')
#f.write('linha 2\n')
#f.write('linha 3\n')

data = f.read()
resp = data.split('\n')

f.close()



f = open('arquivo.txt', 'r')
print(f.read(10))
print(f.read(10))

print(f.readline())

print(f.readline())
print("------------------------")
print(f.readline(4))





f.close()