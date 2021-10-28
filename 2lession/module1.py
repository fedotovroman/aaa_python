def sets_difference(a,b):
    diff = set()
    for el in a:
        if el not in b:
            diff.add(el)
    return(diff)
#print(sets_difference({1,3,4,5},{3,4,5}))


from collections import Counter

def list_difference(a,b):
    x = Counter(a)
    y = Counter(b)
    diff = x - y
    print(list(diff.elements()))
list_difference([1,2,3,4,5,5,5], [1,2,3,4,5])