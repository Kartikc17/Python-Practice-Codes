
#list() : 
li1 = list('Kod')
print(li1) #['K', 'o', 'd']

li2 = list((10,20))
print(li2) # [10, 20] 

li3 = list({100,200})
print(li3) #[200, 100] 

li4 = list({'Name':'Priya', 'age':22})
print(li4) #['Name', 'age']

li5 = list(range(1,11))
print(li5) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print()
#tuple() :
tup1 = tuple([10,20,30])
tup2 = tuple(range(1,11))
tup3 = tuple({100,200})
tup4 = tuple('Kodnest') #('name', 'age')
tup5 = tuple({'name':'Priya','age':22})
print(tup1)
print(tup2)
print(tup3)
print(tup4)
print(tup5)

#set() :

s1 = set([10,20,10,30])
s2 = set(range(1,11))
s3 = set({100,200})
s4 = set('Kodnest') #('name', 'age')
s5 = set({'name':'Priya','age':22})
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)

#dict(iterable_object:key:value)

d1 = dict([['name','Priya'],['age',22]])
print(d1) #{'name': 'Priya', 'age': 22}