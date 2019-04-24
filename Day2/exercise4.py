some_list = ['foo', 'bar', 'baz']
mapping = {}
for i,v in enumerate(some_list):
    mapping[i] = v
print(mapping)

seq1 = ['foo','bar', 'baz']
seq2 = [1, 2, 3]
zipped = zip(seq1, seq2)
print(list(zipped))


for i, (a,b) in enumerate(zip(seq1, seq2)):
    print("{0}: {1}, {2}".format(i,a,b))


print(list(reversed(range(11))))

test_dic = {'a':'1', 'b': [1,2,3,4]}
print(test_dic)
print(test_dic.keys())
print(test_dic.values())
print(test_dic['b'])
print('a' in test_dic) #validates key, not values
print('1' in test_dic)
test_dic.update({'b':'dennis', 'c':300})
print(test_dic)