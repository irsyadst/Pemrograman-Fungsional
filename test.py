""" x = [1, 2, 3]
def fungsi_sederhana(x):
    x[1] = 42
fungsi_sederhana(x)
print(x) """
""" def tambah(*bilangan):
    total = 0
    for n in bilangan:
        total +=n
    return total
print(tambah(1,2,3,4,5,6)) """
""" def connect(**options):
    conn_params = {
        'host': options.get('host', '127.0.0.1'),
        'port': options.get('port', 5432),
        'user': options.get('user', ''),
        'pwd': options.get('pwd', '')
    }
    print(conn_params)
connect()
{'host': '127.0.0.1', 'port': 5432, 'user': '', 'pwd': ''}
connect(port=5432, user='fitti', pwd='nimda')
{'host': '127.0.0.1', 'port': 5432, 'user': 'fitti', 'pwd':'nimda'} """
""" def matrix_mul(a, b):
    return[[sum(i*j for i, j in zip(r, c))
            for c in zip(*b)]for r in a]
a = [[1,2], [3,4]]
b = [[5,1], [2,1]]
c = matrix_mul(a, b)
print(c) """
""" def jumlah(a, b):
    hasil=sum(range(a, b+1))
    return hasil
hasil = jumlah(1, 5)
print(hasil) """
""" list_ku = [4, 10, 3, 0, 7]
test_iter = iter(list_ku)
print(next(test_iter))
print(next(test_iter))
print(next(test_iter))
print(next(test_iter))
print(next(test_iter))
for angka in list_ku:
    print(angka) """
""" def cth_generator(l):
    total=0
    for n in l:
        yield total
        total += n
test_generator=cth_generator([10,20,30,40,50])
print(next(test_generator))
print(next(test_generator))
print(next(test_generator)) """
x1 = 0
x2 = 4
y1 = 5
y2 = 0
import math
def hitung_jarak(x1, y1, x2, y2):
    jarak = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return jarak
jarak = hitung_jarak(x1, y1, x2, y2)
print(f"Jarak antara titik ({x1}, {y1}) dan ({x2}, {y2}) adalah {jarak}")