import itertools
""" a =  [1,2,3,4,5]
print(list(itertools.accumulate(a))) """
""" a = [2,3,0,1]
b = [1,9,2,2]
print(list(itertools.chain(a,b))) """
from itertools import groupby
""" a_list = [("Animal","cat"),
          ("Animal","dog"),
          ("Bird","peacock"),
          ("Bird","pigeon")]
an_iterator = groupby(a_list, lambda x : x[0])
for key, group in an_iterator:
    key_and_group = {key : list(group)}
    print(key_and_group) """
from itertools import filterfalse
""" fruit = ["Apple", "Banana", "pear", "Apricot", "Orange"]
filterfalse = filterfalse(lambda s: s[0] == "A", fruit)
print(list(filterfalse)) """
a=("John","Charles","Mike")
b=("Jenny","Chirsty","Monica","Vicky")
c=list(zip(a,b))
c=list(itertools.zip_longest(a,b))
print(c)