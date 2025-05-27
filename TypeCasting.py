#If string is holding integer then it can be converted into int.
a = '30'
print(a, type(a))
b = int(a)
print(b, type(b))

#String to integer convertion not allowed.
x ='Kod'
print(x, type(x))
#t = int(x)
#print(t, type(t))

#p = float(input('Enter Float type data'))
#print(p, type(p))

#bool() 
q = ''
q = bool(q)
print(q, type(q))
'''
1.while converting int to bool all non zero values we will get true.
2.while converting int to bool for 0 and '' we will get False.
'''
#Taking float value from user and converting it into int 
value = int(float(input('Enter price : Float value ')))
print(value, type(value))