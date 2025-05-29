'''
1. In List we can stroe Homogeneous as well Heterogeneous Data.
2. In List we can store Dublicate value.
3. List is an Ordered Collection of Data: order of insertion will remain
  as it is in the Output.
4. List are immutable: once we declare the list we can not modify it.  
'''

tup1 = (10,22.50,'Kodnest',True,10)
print(tup1)
#tup1.append(100) # error
#tup1.remove(10) # error
#tup1.pop() # error
#del tup[2] # error

# Delete the complete tup1 Object
del tup1 
#print(tup1[2]) # kodnest

t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1 + t2
print(t3) #(1, 2, 3, 4, 5, 6)