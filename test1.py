""" #any()
l = [1, 3, 4, 0]
print (any(l))
l = [0, False]
print (any(l))
l = [0, False, 5]
print (any(l))
l = []
print (any(l))
s = "Hello World!"
print (any(s))
s = '000'
print (any(s))
s = ''
print (any(s)) """
#all()
l = [1, 3, 4, 5]
print (all(l))
l = [0, False]
print (all(l))
l = [1, 3, 4, 0]
print (all(l))
l = [0, False, 5]
print (all(l))
l = []
print (all(l))
s = "Hello World!"
print (all(s))
s = '000'
print (all(s))
s = ''
print (all(s))
""" #zip()
print(list(zip((1, 2, 3), ('a', 'b'))))
coordinate = ['x', 'y', 'z']
value = [3, 4, 5, 0, 9]
result = zip(coordinate, value)
resultList = list(result)
print(resultList) """
""" grocery = ['bread', 'milk', 'butter']
for item in enumerate(grocery):
    print(item)
    print('\n')
for count, item in enumerate(grocery):
    print(count, item)
    print('\n')
        for count, item in enumerate(grocery, 100):
        print(count,item) """