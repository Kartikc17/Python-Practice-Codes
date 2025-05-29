'''
1. In Tuple we can stroe Homogeneous as well Heterogeneous Data.
2. In Tuple we can store Dublicate value.
3. Tuple is an Ordered Collection of Data: order of insertion will remain
  as it is in the Output.
4. Tuple are immutable: once we declare the list we can not modify it.  
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


# Create a Singleton Tuple:
tup = (10,)
print(tup, type(tup)) #10,) <class 'tuple'>

new_tup = (10,20,30,40)
#ele1 = new_tup[0]
#ele2 = new_tup[1]

#unpaking of tuple
ele1,ele2,ele3,ele4 = new_tup
print(ele1,ele2,ele3,ele4)
print('Value of ele:',ele1,ele2)
