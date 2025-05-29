# li = input('Enter space seperated Elements')
# print(li, type(li))
# li = li.split()
# print(li) # ['10', '20', '30', '40'] 
# li = list(map(int, li))
# print(li) # [10, 20, 30, 40]

#user input in one line code:

# tup = tuple(map(int,input('Enter Space seperated Elements ').split()))
# print(tup)

li = list(map(int, input().split()))
print([i for i in li if i%2 == 0])