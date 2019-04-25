import pandas as pd

left = pd.DataFrame({
    'id' : [1,2,3,4,5],
    'name': ['Alex', 'Amy', 'Allen', 'Alice', 'Adam'],
    'subject_id': ['sub1', 'sub2', 'sub3', 'sub4', 'sub5']
})

# print(left)

right = pd.DataFrame({
    'id': [1,2,3,4,5],
    'name': ['ben', 'billy', 'bren', 'brad', 'bob'],
    'subject_id': ['sub2', 'sub4', 'sub3', 'sub6', 'sub5']
})

# print(right)

data = pd.merge(left, right, on='id')
print(data)

data = pd.merge(left, right, on=['id', 'subject_id'])
print(data)

data = pd.merge(left, right, on='subject_id', how='left')
print(data)
data = pd.merge(left, right, on='subject_id', how='right')
print(data)
data = pd.merge(left, right, on='subject_id', how='outer')
print(data)
data = pd.merge(left, right, on='subject_id', how='inner')
print(data)