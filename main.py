 # Задача 1
line = input("Введіть строку:")

def check(a:str):
    return a[::-1]

result = check(line)

if result == line:
    print("Строка є паліндромом")
else:
    print("Строка не є паліндромом")


# Задача 2
number_1 = int(input("Введіть першу цифру:"))
number_2 = int(input("Введіть другу цифру:"))

def plus (num1:int,num2:int):
    return num1 + num2
def minus (num1:int,num2:int):
    return num1 - num2
def deline (num1:int,num2:int):
    return num1 / num2
def multiply (num1:int,num2:int):
    return num1 * num2
def ostatok (num1:int,num2:int):
    return num1 % num2
def deline_2 (num1:int,num2:int):
    return num1 // num2
def multiply_2 (num1:int,num2:int):
    return num1 ** num2

result_op = input("Яку операцію робимо ? +,-,*,//,%,:")

if result_op == "+" :
    print(plus(number_1,number_2))

elif result_op == "-" :
    print(minus(number_1,number_2))

elif result_op == "*" :
    print(multiply(number_1,number_2))

elif result_op == "/" :
    print(deline(number_1,number_2))

elif result_op == "**" :
    print(multiply_2(number_1,number_2))

elif result_op == "%" :
    print(ostatok(number_1,number_2))

elif result_op == "//" :
    print(deline_2(number_1,number_2))

else:
    print("Ви ввели щось неправильно !")
