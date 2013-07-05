# Please fill out this stencil and submit using the provided submission script.





## Problem 1
def myFilter(L, num):
    M = [x for x in L if x % 2 == 0]
    return M


## Problem 2
def myLists(L):
    result = []
    for x in L:
        for i in range(
    


## Problem 3
def myFunctionComposition(f, g):
    gof = dict()
    for k in f.keys():
        gof[k] = g[f.get(k)]
    return gof


## Problem 4
# Please only enter your numerical solution.

complex_addition_a = ... 
complex_addition_b = ...
complex_addition_c = ...
complex_addition_d = ...



## Problem 5
GF2_sum_1 = ...
GF2_sum_2 = ...
GF2_sum_3 = ...


## Problem 6
def mySum(L): pass
    suma = 0
    for x in L:
        suma = suma + x
    return x


## Problem 7
def myProduct(L): pass
    producto = 1
    for x in L:
        producto = producto * x
    return producto


## Problem 8
def myMin(L):
    min = L[0]
    for i in range(1,len(L)):
        if L[i] < min:
            min = L[i]
    return min


## Problem 9
def myConcat(L):
    concat = ""
    for s in L:
        concat = concat + s
    return concat


## Problem 10
def myUnion(L):
    union_ = set()
    for set_ in L:
        union_.union(set_)
    return union_
