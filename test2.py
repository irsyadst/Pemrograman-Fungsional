""" kuadrat = lambda x: x*x
print(kuadrat(3))
kali = lambda x, y: x*y
print(kali(4,3)) """
""" f = lambda x, y, z: x + y + z
print(f(2, 30, 400)) """
""" L = [lambda x: x ** 2,
     lambda x: x ** 3,
     lambda x: x ** 4]
for f in L:
    print(f(3))
    print(L[0](11)) """
""" nilai = [1, 2, 3, 4, 5]
pangkat = []
for x in nilai:
    pangkat.append(x**2)
    print(pangkat) """
""" nilai = [1, 2, 3, 4, 5]
def pangkat(x)  : return x**2
print(list(map(pangkat, nilai))) """
""" my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x*2, my_list))
print(new_list) """
""" my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0), my_list))
print(new_list)  """
X = [2, 4, 6, 8]
Y = [1, 3, 5, 10]

print(sum(map(lambda x, y: abs((x - y)**2 / len(X)), X, Y)))