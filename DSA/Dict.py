'''
1. In Dict we can stroe Homogeneous as well Heterogeneous Data.
2. In Dict we can store Dublicate value but not Dublicate Kyes.
3. Dict is an Ordered Collection of Data: order of insertion will remain
  as it is in the Output.
4. List are mutable: once we declare the list we can modify it.  
'''

d1 = {'name':'Priya', 'age':27 , 'phone':3443}
print(d1, type(d1)) # {'name': 'Priya', 'age': 27, 'phone': 3443} <class 'dict'>


d1['name'] ='pooja'
print(d1) # {'name': 'pooja', 'age': 27, 'phone': 3443}

marks = {'sci': 85, 'Math':85} # Allowd

for i in d1.keys():
    print(i)
print()
for i in d1.values():
    print(i)
print()
for i in d1.items():
    print(i)


