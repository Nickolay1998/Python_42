class AgeError(Exception):
   def __init__(self, value):
       self.value = value
       super().__init__(f"{self.value}")

name = "Nick"
age = int(input("Your age: "))
if age<0 or age>130:
    raise AgeError("Not correct age")
else:
    print(f"Hello,{name}! your age - {age}")

class AgeError(Exception):
   def __init__(self, value):
       self.value = value
       super().__init__(f"{self.value}")
#
# name = "Nick"
# age = int(input("Your age: "))
# def agef(name, age):
#    if age<0 or age>130:
#        raise AgeError("Not correct age")
#    else:
#        return f"Hello,{name}! your age - {age}"
#
# print(agef(name, age))

# class AgeError(Exception):
#    def __init__(self, value):
#        self.value = value
#        super().__init__(f"{self.value}")
#
# def agef(name, age):
#     return f"Hello,{name}! your age - {age}"
#
# name = "Nick"
# age = int(input("Your age: "))
# if age<0 or age>130:
#     raise AgeError("Not correct age")
# else:
#     print(agef(name, age))

# class Negativenumber(Exception):
#    def __init__(self, value):
#        self.value = value
#        super().__init__(f"{self.value}")
#
# numbers = input("Enter a numbers: ")
# list_numbers = [int(i) for i in numbers.split()]
# print(list_numbers)
#
# l = []
# for i in range(len(list_numbers)):
#     if list_numbers[i] < 0:
#         raise Negativenumber("Must be positive")
#     else:
#         l.append(list_numbers[i])
# print("summ positive numbers",sum(l))




# class Negativenumber(Exception):
#    def __init__(self, value):
#        self.value = value
#        super().__init__(f"{self.value}")
# def listf(list_numbers):
#     return list_numbers
#
# numbers = input("Enter a numbers: ")
# list_numbers = [int(i) for i in numbers.split()]
# print(list_numbers)
#
# l = []
# for i in range(len(listf(list_numbers))):
#     if listf(list_numbers[i]) < 0:
#         raise Negativenumber("Must be positive")
#     else:
#         l.append(list_numbers[i])
#print("summ positive numbers",sum(l))

# class Negativenumber(Exception):
#    def __init__(self, value):
#        self.value = value
#        super().__init__(f"{self.value}")
#
# numbers = input("Enter a numbers: ")
# list_numbers = [int(i) for i in numbers.split()]
#
# def listf(list_numbers):
#     print(list_numbers)
#     l = []
#     for i in range(len(list_numbers)):
#         if list_numbers[i] < 0:
#             raise Negativenumber("Must be positive")
#         else:
#             l.append(list_numbers[i])
#     print("summ positive numbers",sum(l))
#
# listf(list_numbers)

