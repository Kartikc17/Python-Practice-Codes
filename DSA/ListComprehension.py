#without ListComprehension
li1 = [1,2,3,4,5]
print(li1)
sq_li = []
for i in li1:
    sq_li.append(i**2)
print(sq_li)

print()
# Sysntax: [expression for i in iterable_object condition]
# only if condition is there (after for loop if comes)
dublicate_li1 =  [i for i in li1]
print(dublicate_li1)
even = [i for i in li1 if i%2 == 0]
print(even)
sq_list = [i**2 for i in li1]
print(sq_list)
new_li1 = [i+2 for i in li1]
print(new_li1)

# if both if-else condition is there (before for loop if - else comes)
#Syntax: [ 'if return value' if condition else condition 'else return value' for i in iterable_objec]
even_odd = ['even' if i%2 == 0 else 'odd' for i in li1]
print(even_odd)

#Multiple for loop inside list comprehension
li = [[10,20],[30,40],[50,60]]
new_li = [ele for sublist in li for ele in sublist]
print(new_li)

'''
Q. r1 = upper limit 1 (0,1)
   r2 = upper limit 2 (0,1,2)
   r3 = upper limit 1 (0,1)
sum should not == 2
   (0,0,0)(0,0,1)(0,1,0)(1.1.1)
'''
r1 = 1
r2 = 2
r3 = 1
res = [[i,j,k] for i in range(r1+1) for j in range(r2+1) for k in range(r3+1) if i+j+k != 2]
print(res)