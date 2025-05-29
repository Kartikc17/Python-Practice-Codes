'''
1.Conditional: if-else, if-elif
2.Looping: for, while
3. Jumping: break, continue, pass
'''

print("if- else------------------------------")
def checkAge(age):
    if(age > 18):
        print('Age is greater than 18')
    else:
        print('Age is not greater than 18')
checkAge(15)

print("if-elif---------------------------------")
def displyAge(age):
    if(age < 18):
        print('chile')
    elif(age > 18 and age < 65):
        print('Adult')
    elif(age >= 65):
        print('senior Citizen')
displyAge(int(input("Enter age: ")))


'''
for control_variable in iterable_object
'''
print("for loop-------------------------------")
for i in 'KodNest':
    print(i,end=' ')
  
for j in [10,20,30]:
    print(j+5, end=' ')

for num in range(1,11):
    print(num, end=' ')

for num in range(11,21,2):  #step parameter(i+2).
    print(num, end=" ")
    
print("\n.....................")

for i in range(5):
    print(i, end=" ")

print("\n......................")

for i in range(1,11):
    if(i % 2 == 0):
        print(i, end=' ')


# while loop: 
print("\nWhile loop-----------------------------")

i = 0;
while(i < 10):
    print(i+100, end=' ')
    i = i + 1

# jumping contructs:
print("\nJumping.........skip...........")

for i in range(1, 11):
    if(i == 6):
        continue
    print(i, end=' ')
print("\n.............stop....")
for i in range(1,11):
    if(i == 5):
        break
    print(i, end=' ')

#use of pass
print('\n.....pass......')
def disp():
    pass

class Demo:
    pass