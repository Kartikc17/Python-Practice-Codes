'''
1. In List we can stroe Homogeneous as well Heterogeneous Data.
2. In List we can store Dublicate value.
3. List is an Ordered Collection of Data: order of insertion will remain
  as it is in the Output.
4. List are mutable: once we declare the list we can modify it.  
'''

li1 = [10,44,23.12,True,'Kodnest', 10]
print(li1, type(li1))

#append(): will add elements at the wndof the list.
li1.append(300)
print(li1)

#insert(index, element): insert an ele at specified index.
li1.insert(1, 15)
print(li1) 

#remove(ele) :  Remove the first occurence of the specified ele.
li1.remove(10)
print(li1)

# in and not in Operators:
print(200 in li1) #false
print('Kodnest' in li1) # True 

#pop(): Without argument will delete and return last ele from list
removed_ele = li1.pop()
print(removed_ele) # 300
print(li1) # [15, 44, 23.12, True, 'Kodnest', 10]

#pop(index) : with argument will delete the ele. at specified index
removed_ele = li1.pop(4)
print(removed_ele) #Kodnest
print(li1) #[15, 44, 23.12, True, 10]

# del keyword :del index ele and  wont return del ele
del li1[1]
print(li1) # 

del li1
print(li1) # error: name 'li1' is not defined