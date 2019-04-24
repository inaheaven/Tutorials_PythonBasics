a = ['a', 'b', 'c']
b = ['c', 'd']
c = a + b
print(c)


a = [1,2,3,4,5]
print(a[0:2])
b = a[:2]
print(b)
c = a[2:]
print(c)

list1 = ['hi', 'test', 1990, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c"]

print("list1", list1)

list1[2] = 20
print("list1: 2~3", list1[2:3])


a = [1, 'a', 'b', 'c', 4]
a[1:3] = []
print(a)

#append

a = [1,2,3]
a.append(4)
print(a)

#reverse
a.reverse()
print(a)

#insert
a=[1,2,3]
a.insert(0,4)
print(a)

a = [1,2,3]
a.pop()
print(a)

a=[1,2,3,1]
print(a.count(1))

#extend -- list append
a = [1,2,3]
a.extend([4,5])
print(a)

#tuple handling is different from list. it goes with ()
#tuple is immutable, meaning can't be changed.

t1 = (1,2,3,4)
t2 = (3,4)
print(t1+t2)
#t1[0] = 4 will cause error as it is immutable

