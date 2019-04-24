money = 2000
card = 1
if money >= 3000 or card >= 1:
    print('taxi')
else:
    print('walk')

var = 100
if(var == 100):
    print("check 100")

if(var == 200):
    print("check 200")
else:
    print("check200 failed")

count = 0
while(count<9):
    print('count is', count)
    count = count+1
print("exit")

var = 1
while var == 1:
    num = int(input("Enter a number:"))
    print("num", num)
    var += 1

print("exit")

count = 0
while count<5:
    print(count, "is less than 5")
    count = count+1
else:
    print(count, "is or greater than 5")


pocket = ['paper', 'cellphone, money']
if 'money' in pocket:
    pass
else:
    print("can't pass")

menus = ['pizza', 'ramen', 'cora']
if 'pizza' in menus:
    print("I will eat this pizza")
else:
    print("Can't eat pizza because i dont have it")
print("done with pizza")

pocket = ['paper', 'cell']
card =1
if 'money' in pocket:
    print("will pay for the taxi")
elif 'cell' in pocket:
    print("call your friend to pick up")
else:
    print("wave your hands for the help")

amount = int(input("Enter amount"))
if amount < 1000:
    discount = amount * 0.5
    print("discount", discount)
else:
    discount = amount * 0.9
    print("discount", discount)
print("netpayable", amount-discount)

test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

for letter in 'python':
    if letter == 'h':
        pass
        print("this is pass h block")
    print(letter)

sum =0
for i in range(1,11):
    sum = sum +i
    print(sum)

for i in range(2,10):
    print(i)
    for j in range(1,10):
        print(i, "X", j, i*j)
