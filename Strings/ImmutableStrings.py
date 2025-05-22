'''Stirngs are Immutble:

1.Once we declare the string we connot modify it, 
if we try to modify the string will create new string.

2. if string dose not have any ref variable then it will be removed.
3.Python Internally uses string Interning.

4. String iterning is the process of checking string intern pool
before creating new object.

however we want to crate new object, Python first will check string intern pool,
wheather that object already exist or not.

When Object alredy exist in the string intern records the adderss 
of existing object will be reused.
'''

#s1 = 'kodnest'
#s1 = s1.upper()
#print(s1)

#s1 = 'K'
#print(s1, id(s1))

s1 = 'Hello'
s2 = 'World'

print(s1, id(s1))
print(s2, id(s2))

print('ID of s1.H: ',id(s1[0]))
print('ID of s1.o: ',id(s1[-1]))

print('ID of W:', id(s2[0]))
print('ID of o:', id(s2[1]))

print('s1 ID of l:', id(s1[2]))
print('s1 ID of l:', id(s1[3]))
print('s2 ID of l:', id(s2[3]))
