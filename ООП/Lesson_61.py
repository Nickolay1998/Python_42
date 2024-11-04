# Винятки

# https://python.readthedocs.io/en/stable/library/exceptions.html

# 1
# while True:
#     number1 = int(input("Enter a number1: "))
#     command = str(input("Enter command: "))
#     number2 = int(input("Enter a number2: "))
#     if command == '+':
#         print(number1 + number2)
#     elif command == '-':
#         print(number1 - number2)
#     elif command == '*':
#         print(number1 * number2)
#     elif command == '/':
#         print(number1 / number2)

# 2
# while True:
#     number1 = ''
#     number2 = ''
#     while not number1.isdigit():
#         number1 = input("Enter a number1: ")
#     number1 = int(number1)
#     command = str(input("Enter command: "))
#     while not number2.isdigit():
#         number2 = input("Enter a number2: ")
#     number2 = int(number2)
#     if command == '+':
#         print(number1 + number2)
#     elif command == '-':
#         print(number1 - number2)
#     elif command == '*':
#         print(number1 * number2)
#     elif command == '/' and number2 != 0:
#         print(number1 / number2)

# 3
# while True:
#     try:
#         number1 = int(input("Enter a number1: "))
#         command = str(input("Enter command: "))
#         number2 = int(input("Enter a number2: "))
#         if command == '+':
#             print(number1 + number2)
#         elif command == '-':
#             print(number1 - number2)
#         elif command == '*':
#             print(number1 * number2)
#         elif command == '/':
#             print(number1 / number2)
#     except ValueError:
#         print("Incorrect value")
#     except ZeroDivisionError:
#         print("Zero Division ")
#     except BaseException:
#         print("Some error")
#     else:
#         print("Your calculation was successful")
#     finally:
#         print("Goodbye")

# try:
#     print(2/0)
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# except ArithmeticError:
#     print("ArithmeticError")
# except Exception:
#     print("Exception")
# except BaseException:
#     print("BaseException")

# Task 1
'''Напишіть програму, яка дозволяє користувачеві обчислити частку
(ділення одного числа на інше) двох чисел.
Програма приймає два значення з клавіатури і повертає
результат операції на екран. Обробіть виняток,
що виникає під час ділення на нуль, і виведіть повідомлення про помилку.'''

number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))
try:
    print(number1 / number2)
except ZeroDivisionError:
    print("На ноль делить")

# Task2
'''Реалізуйте перше завдання через функцію. Функція повинна приймати два параметри 
і відображати результат ділення на екран. Створіть дві версії реалізації функції:
Перша версія не обробляє виняток усередині функції. Уся обробка знаходиться зовні;
Друга версія обробляє виняток усередині функції.'''


# 1
def f1(number1, number2):
    return number1 / number2


number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))
try:
    print(f1(number1, number2))
except ZeroDivisionError:
    print("На ноль делить")


# 2
def f2(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "На ноль делить нельзя"


x = int(input("num1"))
y = int(input("num2"))
print(f2(x, y))
