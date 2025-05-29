# Object.reverse() will reverse the original object.
li = [10,5,30,20,40]
print('Before Reverse:',li)
li.reverse()
print('After Reverse:',li) #[40, 20, 30, 5, 10]

#list(reversed(object)): iterable_object
li2 = [11,3,35,3,6]
reverse_li2 = list(reversed(li2))
print(reverse_li2)


li3 = [1,5,2,9]
new_li3 = list(reversed(li3)) # creating new reverse list
li3.reverse() # reversing original list
print(li3)
print(new_li3)