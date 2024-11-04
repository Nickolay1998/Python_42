# Дескриптори
# class VerboseAttribute:
#     def __init__(self, name):
#         self.name = name
#
#     def __get__(self, obj, objtype):
#         value = obj.__dict__[self.name]
#         return value.upper()
#
#     def __set__(self, obj, value):
#         obj.__dict__[self.name] = value
#
# class PhoneValidation(VerboseAttribute):
#     def __set__(self, obj, value):
#         if ('+380' in value) and (len(value) == 13):
#             obj.__dict__[self.name] = value
#         else:
#             obj.__dict__[self.name] = '+380631234567'
#
# class Book:
#     title = VerboseAttribute('title')
#     author = VerboseAttribute('author')
#     phone_number = PhoneValidation('phone_number')
#
# book = Book()
# book.title = 'A Byte of Python'
# book.phone_number = '+380639124589'
# print(book.title)
# print(book.phone_number)
#
# class OneTimeReadDescription:
#     def __init__(self, name):
#         self.name = name
#         self.accessed = False
#
#     def __set__(self, obj, value):
#         obj.__dict__[self.name] = value
#
#     def __get__(self, obj, objtype):
#         if self.accessed:
#             raise Exception('Access denied you use your one try to access')
#         else:
#             self.accessed = True
#             return obj.__dict__[self.name]
#
# class SecretData:
#     secret_attribute = OneTimeReadDescription('secret_attribute')
#
# some_secret_element = SecretData()
# some_secret_element.secret_attribute = '123'
# print(some_secret_element.secret_attribute)
# input()
# print(some_secret_element.secret_attribute)
#
# class Singleton:
#     _instance = None
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
#     def __init__(self, *args, **kwargs):
#         self.args = args
#
#     def __str__(self):
#         return f'{self.args}'
#
# a = Singleton(5)
# b = Singleton(1)
# print(a is b)
#
# print(a)
#
# c = Singleton(6)
# print(a)
# Записна книжка

class Note:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content

    def edit(self, new_content):
        self.content = new_content

    def __str__(self):
        return self.content
class Notebook:

    # Create notes
    def __init__(self):
        self.notes = []

    # Create note
    def add_note(self, title, author, content):
        note = Note(title, author, content)
        self.notes.append(note)

    # Read
    def __str__(self):
        result = ''
        for note in self.notes:
            result = result + str(note.content) + '\n'
        return result

    # Delete
    def remove_note(self, title):
        for index in range(len(self.notes)):
            if (self.notes[index]).title == title:
                self.notes.pop(index)
                break
flag = True
book = Notebook()

while flag:
    command = str(input('Enter command: [r], [c], [e], [d]: '))
    if command.lower() == 'c':
        title = str(input('Enter title: '))
        author = str(input('Enter author: '))
        content = str(input('Enter content: '))

        book.add_note(title, author, content)
    elif command.lower() == 'r':
        print(book)

    elif command.lower() == 'e':
        flag = str(input("Enter [any key] + [enter] to continue OR enter [enter] to exit: "))

    elif command.lower() == 'd':
        title = str(input('Enter title: '))
        book.remove_note(title)

# age = 12
# if age < 13:
#     print('Child')
