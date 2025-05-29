'''
1. In Set we can stroe Homogeneous as well Heterogeneous Data.
2. In Set we can not store Dublicate value.
3. Set is an UnOrdered Collection of Data: order of insertion will not remain
  as it is in the Output.
4. Set are mutable: once we declare the list we can modify it. 
5. Set does not support indexing of data.
'''

s1 ={10,True,'Kodnest',10,20,55.44}
print(s1, type(s1)) #{True, 20, 55.44, 'Kodnest', 10} <class 'set'>
#print(s1[0]) #Error

#add()
s1.add(500)
print(s1) # {True, 'Kodnest', 20, 500, 55.44, 10}

s1.remove(55.44)
print(s1) #{True, 20, 500, 10, 'Kodnest'}

#pop without index will delete and return ele
popped_ele = s1.pop()
print(popped_ele) # True
print(s1) # {20, 500, 10, 'Kodnest'}

del s1