# class SevenError(Exception):
#     def __init__(self, value):
#         self.value = value
#         super().__init__(f"{self.value}")
#
#
# a = 5
# b = 2
#
#
# def plus(a, b):
#     result = a + b
#     if result == 7:
#         raise SevenError("You cannot use 7")
#     else:
#         return result
#
#
# print(plus(a, b))


class HeavySize(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"{self.value}")

def check(l):
    if l.__sizeof__() > 128:
        raise HeavySize("You cannot use size more 128")
    else:
        return l

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
try:
    print(check(l))
except HeavySize:
    print("Heavy size")
except:
    print("Something went wrong")

class NumberMoreLimit(Exception):
    def __init__(self,value):
        self.value = value
        super().__init__(f"{self.value} is more")

def limit_num(l):
    if len(l) > 1000:
        raise NumberMoreLimit(l)
    else:
        return l

l=[i for i in range(1,1003)]
print(l)
try:
    print(limit_num(l))
except NumberMoreLimit:
    print("a lot of numb")
except:
    print("something went wrong")

class NegativeNumberError(Exception):
    def __init__(self, message="Number cannon be negative"):
        self.message = message
        super().__init__(self.message)

def check_positive_number(num):
    if num < 0:
        raise NegativeNumberError
    else:
        print('Positive')

try:
    number = float(input("Input number "))
    check_positive_number(number)
except NegativeNumberError:
    print('Negative')
except ValueError:
    print("Error")

class StrFirst(Exception):
    def __init__(self,value):
        self.value = value
        super().__init__(f"{self.value} is first")

def firs_str(text):
    if text[0] != str(text[0].upper()):
        raise StrFirst(text)
    else:
        return text

def firs_str1(text):
    if not text[0].isalpha():
        raise StrFirst(text)
    else:
        return text

text="vanya love pepsi cola"
try:
    print(firs_str(text))
except StrFirst:
    print("first verb not apper")
except :
    print("Error")