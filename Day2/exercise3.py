##tuple seq and data slicing

tup = 4,5,6
print(tup)

nested_tup = (4,5,6),(7,8)
print(nested_tup)

tup2 = tuple('hello')
print(tup2)
print(tup2[0])

tup3 = tuple(['foo', [1,2], True])
print(tup3)

# tup3[2] = False --> tup can't be changed

print(tup3[2])

tup3[1].append(3)
print(tup3)


tup4 = (4,5,6)
a, b, c = tup
print(tup)
print(a)
print(b)
print(c)

tup5 = (4,5, (6,7))
print(tup5)
print(tup5[2])

seq = [(1,2,3), (4,5,6), (7,8,9)]
print(seq)
for a, b, c in seq:
    print('a={0}, b={1}, c={2}'.format(a,b,c))

values = 1,2,3,4,5
a,b, *rest = values
print(values)
print(a,b)
print(rest)

a = (1,2,3,4,5)
print(a.count(2))

a_list = [2,3,7, None]
print(a_list)


tub = ('foo', 'bar', 'baz')
b_list = list(tub)
print(b_list)
b_list[1] = 'test'
print(b_list)

gen = range(10)
print(list(gen))
c_list = list(gen)
print(c_list)
c_list.append(10)
print(c_list)

c_list.pop(3)
print(c_list)
c_list.remove(9)
print(c_list)

print(8 in c_list)
print(9 in c_list)

d = [4, None, 'foo'] + [7,8,(2,3)]
print(d)

e = [4,None,'foo']
e.extend([5,6,(2,3)])
print(e)

f = [7,2,5,4]
print(f)
f.sort()
print(f)

g=['saw', 'small', 'he', 'site']
g.sort(key=len)
print(g)

seq = [7,8,2,1,2,3,5]
print(seq)
print(seq[3:4])
seq[3:4] = [6,3]
print(seq)
print(seq[-6:-2])
print(seq[-6:-1])
print(seq[-6:0])
print(seq[::-1])