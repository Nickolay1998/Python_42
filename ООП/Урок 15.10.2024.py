                                                              #Функтори
class Event:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.attendees = []

    def add_attendee(self, person):
        self.attendees.append(person)

    def __repr__(self):
        return f'Event ({self.name}, {self.location})'

    def __str__(self):
        return f'{self.name} at {self.location} with {len(self.attendees)} attendees'

event = Event('Python Workshop', 'Odesa')
event.add_attendee('John Doe')
event.add_attendee('Jane Doe')
print(event)


##class Course:
##    _namecourse = ["Programs","PCcourse","C++"]
##    _students = ["student1","student2","student3"]
##    _results = [10,11,12]
##
##    def res(self):
##        return f"{(self._results[0]+self._results[1]+self._results[2])/len(self._results)}"
##c = Course()
##print(c.res())

##class Course:
##    def __init__(self, name):
##        self.name = name
##        self.courses=[]
##        self.grade = []
##    def add_grade(self, grade):
##        self.grade.append(grade)
##    def add_course(self, course):
##        self.courses.append(course)
##
##
##    def __repr__(self):
##        return f"Course ({self.name}, {self.grade})"
##
##    def __str__(self):
##        return f"{self.name} at {self.grade}"
##
##course=Course("Petrov")
##course.add_grade("Python")
##course.add_grade(10)
##print(course)

##class Course:
##    def __init__(self, course_name):
##        self.course_name=course_name
##        self.student_name=[]
##        self.grades=[]
##
##    def add_student(self,student_name,grade):
##        self.student_name.append(student_name)
##        self.grades.append(grade)
##
##    def average_grade(self):
##        avg=sum(self.grades)/len(self.grades)
##        return avg
##course=Course('Math')
##
##course.add_student('Ivan Ivanov',85)
##course.add_student('Oleg Petrov',87)
##print(course.average_grade())
import time


##class Timer:
##    def __init__(self):
##        self.start_time = None
##        self.end_time = None
##
##    def start(self):
##        self.start_time = time.time()
##
##    def stop(self):
##        self.end_time = time.time()
##        return self.end_time - self.start_time
##
##    def result(self):
##        return self.end_time - self.start_time
##
##    def __str__(self):
##        result = self.end_time - self.start_time
##        return f'{result}'


##class Adder:
##    def __init__(self, num):
##        self.num = num
##
##    def __call__(self, addnum):
##        return self.num + addnum
##
##
##a = Adder(10)
##print(a(10))
##print(a(30))

### Декоратори в рамках ООП
##import time
##def debug(func):
##    def wrapper(*args, **kwargs):
##        result = func(*args, **kwargs)
##        print(f"Calling: {func.__name__}({args}, {kwargs}) Result: {result}")
##        return result
##
##    return wrapper
##
##def timer(func):
##    def wrapper(*args, **kwargs):
##        start_time = time.time()
##        result = func(*args, **kwargs)
##        end_time = time.time()
##        print(f"Calling: {func.__name__}({args}, {kwargs}\n Time: {end_time-start_time}")
##        return result
##    return wrapper
##
##class Calculator:
##    @debug
##    def add(self, x, y):
##        return x + y
##
##    @timer
##    def square(self, x):
##        return x * x
##
##calc = Calculator()
##print(calc.add(2, 3))
##print(calc.square(42))
# Декоратори в рамках ООП
##import time
##
##
##def debug(func):
##    def wrapper(*args, **kwargs):
##        result = func(*args, **kwargs)
##        print(f"Calling: {func.__name__}({args}, {kwargs}) Result: {result}")
##        return result
##
##    return wrapper
##
##
##def timer(func):
##    def wrapper(*args, **kwargs):
##        start_time = time.time()
##        result = func(*args, **kwargs)
##        end_time = time.time()
##        print(f"Calling: {func.__name__}({args}, {kwargs}\n Time: {end_time - start_time}")
##        return result
##
##    return wrapper
##
##def logger(func):
##    def wrapper(*args, **kwargs):
##        start_time = time.time()
##        result = func(*args, **kwargs)
##        end_time = time.time()
##        f = open('results.txt', 'at')
##        f.write(f"Calling: {func.__name__}({args}, {kwargs}\n Time: {end_time - start_time}\n\n")
##        f.close()
##        return result
##    return wrapper
##
##
class Calculator:
    @debug
    def add(self, x, y):
        return x + y

    @timer
    def square(self, x):
        return x * x

    @logger
    def simple(self, n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

calc = Calculator()
print(calc.add(2, 3))
print(calc.square(42))
print(calc.square(41))
print(calc.simple(115249))
##def uppercase(func):
##    def wrapper(*args, **kwargs):
##        result = func(*args, **kwargs).upper()
##        print(f"Calling: {func.__name__}({args}, {kwargs})Result: {result}")
##        return result
##    return wrapper
##
##
##class Human:
##    def __init__(self, name, surname):
##            self.name = name
##            self.surname = surname
##    @uppercase
##    def display_name(self):
##            return f'{self.name} {self.surname}'
##
##sten = Human('Sten', 'Kubrik')
##print(sten.display_name())



##class Person:
##    def __init__(self, first_name, last_name):
##        self.first_name = first_name
##        self.last_name = last_name
##    @property
##    def full_name(self):
##        return f'{self.first_name} {self.last_name}'
##
##    @full_name.setter
##    def full_name(self, name):
##        first_name, last_name = name.split(' ')
##        self.first_name = first_name
##        self.last_name = last_name
##
##
##person = Person('John', 'Doe')
##print(person.full_name)
##print(person.first_name)
##print(person.last_name)
