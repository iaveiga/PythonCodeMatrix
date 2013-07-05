## Task 1 OK
minutes_in_week = 7 * 24 *60

## Task 2 OK
remainder_without_mod = 2304811 - (2304811 // 47) * 47

## Task 3 OK
divisible_by_3 = (673 + 909) % 3 == 0

## Task 4 OK
x = -9 
y = 1/2
statement_val = 1

## Task 5 OK
first_five_squares = { x * x for x in {1,2,3,4,5} }

## Task 6 OK
first_five_pows_two = { 2 ** x for x in {0,1,2,3,4} }

## Task 7: enter in the two new sets OK
X1 = { 5, 7, 9 }
Y1 = { 2, 4, 6 }

## Task 8: enter in the two new sets OK
X2 = { 0, 1, 2 }
Y2 = { 4, 8, 16 }

## Task 9 OK
base = 10
digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
three_digits_set = { x * (base ** 2) + y * (base ** 1) + z * (base ** 0) for x in digits for y in digits for z in digits}

## Task 10 OK
S = {1, 2, 3, 4}
T = {3, 4, 5, 6}
S_intersect_T = { x for x in S if x in T  }

## Task 11 OK
L_average = sum(L)/len(L) 

## Task 12 OK
LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
LofL_sum = sum(sum(x) for x in LofL)

## Task 13 OK
cartesian_product = [[x,y] for x in {'A','B','C'} for y in {1,2,3}]

## Task 14 OK
S = {-4, -2, 1, 2, 5, 0}
zero_sum_list = [d for d in [(i,j,k) for i in S for j in S for k in S] if sum(d) == 0]

## Task 15 OK
exclude_zero_list = [d for d in [(i,j,k) for i in S for j in S for k in S] if sum(d) == 0 and d !=(0,0,0)]

## Task 16 OK
first_of_tuples_list = [d for d in [(i,j,k) for i in S for j in S for k in S] if sum(d) == 0 and d !=(0,0,0)][0]
                     
## Task 17 Partial
L1 = [1,1,2] 
L2 = [1,1,2] 

## Task 18 OK
odd_num_list_range = list(range(1,100,2))

## Task 19 OK
L = ['A','B','C','D','E']
range_and_zip = [(a,b) for (a,b) in zip(range(0,6),L)]

## Task 20 OK
list_sum_zip = [ a + b for a,b in zip([10,25,40],[1,15,20])]


## Task 21
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
value_list = [ ]

## Task 22
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
k = 'Bilbo'
value_list_modified_1 = [ ] # <-- Use the same expression here
k = 'Frodo'
value_list_modified_2 = [ ] # <-- as you do here

## Task 23 OK
square_dict = {x: x * x for x in range(0,100)}

## Task 24 OK
D = {'red','white','blue'}
identity_dict = {x : x for x in D}

## Task 25 OK
base = 10
digits = set(range(10))
representation_dict = {x : [ [x,y,z] for x in digits for y in digits for z in digits][x] for x in range(base ** 3)}

## Task 26
d = {0:1000.0, 1:1200.50, 2:990}
names = ['Larry', 'Curly', 'Moe']
listdict2dict = {  }

## Task 27 OK
def nextInts(L): return [ i + 1 for i in L ]

## Task 28 OK
def cubes(L): return [ i ** 3 for i in L ]

## Task 29 OK
def k (dct,keylist): return [ dct.get(key) for key in keylist ]

## Task 30 OK
def list2dict(L, keylist): return {keylist[i] : L[i]  for i in range(0,len(L))}
