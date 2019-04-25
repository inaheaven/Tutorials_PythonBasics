#dictionary: associative array or hash. you get value with key
dic = {'name':'lenny', 'phone':'010-9133', 'birth':'880602'}
print(dic)



a = {'name': 'a'}
a[2] = 'b'
print(a)
a = {'name': 'pey', 3:[1,2,3], 2: 'b'}
print(a)
del a[2]
print(a)

print(a.keys())
print(a.values())
print(a.items())
print(a.get('name'))
print('name' in a)


#중복을 허용하지 않는다.
#순서가 없다(Unordered)

s1 = set([1,2,3])
print(s1)

#순서가 없고 중복이 허용되지 않는다. 같은 데이터를 넣더라도 처리가 달라진다.
s2 = set("Hello")
print(s2)

#교집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,6,7,8])

print(s1&s2)
print(s1-s2)
print(s1.difference(s2))
s1.add(7)
print(s1)



a = [1,2,3,4]
while a:
    b = a.pop()
    print(b)
