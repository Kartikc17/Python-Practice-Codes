#input() always takes an input as a string, if want in int do typecasting
#Division result will always be of type float.
num1 = int(input('Enter the num1 : \n'))
num2 = int(input('Enter the num2 : \n'))

print(f'Addition of {num1} and {num2} is {num1+num2}')
print(f'Subtraction of {num1} and {num2} is {num1-num2}')
print(f'Multiplication of {num1} and {num2} is {num1*num2}')
print(f'Division of {num1} and {num2} is {num1/num2}')