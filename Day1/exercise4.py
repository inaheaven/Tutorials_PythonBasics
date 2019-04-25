def sum(a,b):
    result = a+b
    return result
a = sum(3,4)
print(a)


def say():
    return 'hi'

print(say())


def changeme(mylist):
    print(mylist)
    mylist[2] = 50
    print(mylist)
mylist = [10,20,30]
changeme(mylist)

def printinfo(arg1, *var1):
    print("out value")
    print(arg1)
    for v in var1:
        print(v)
    return

printinfo(10)
printinfo(70, 60, 50)

#lambda makes anonymous function
sum = lambda arg1, arg2: arg1 + arg2
print("result", sum(1,2))


#file 작성

f = open("exercise4.txt", 'w')
for i in range(1,11):
    data = "%d 번째 줄입니다. \n" %i
    f.write(data)
f.close()

print(f.name)
print(f.closed)
print(f.mode)


f = open("exercise4.txt", "r")
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open("exercise4.txt", "a")
data = "add this"
f.write(data)
f.close()