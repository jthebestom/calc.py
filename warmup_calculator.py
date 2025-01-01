print('this is calculator')


command = input('+,-,/,*: enter command: ')
x = int(input("first num: "))
y = int(input("second num: "))

def add(x,y):
    print(x+y)

def divide(x,y):
    print(x/y)

def multiply(x,y):
    print(x*y)

def subtract(x,y):
    print(x-y)

if command == '+':
    add(x,y)

elif command == '-':
    subtract(x,y)

elif command == '/':
    divide(x,y)
    
elif command == '*':
    multiply(x,y)




# if command == "+":
#     print(x+y)
# elif command == "-":
#     print(x-y)
# elif command == "/":
#     print(x/y)
# elif command == "*":
#     print(x*y)



    


