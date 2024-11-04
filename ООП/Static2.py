# class Drob:
#     count = 0
#     def __init__(self, x,y):
#         self.x = x
#         self.y = y
#         Drob.count += 1
#
#     @staticmethod
#     def countobjects():
#         return Drob.count
#
# D1=Drob(3,4)
# D2=Drob(5,7)
# D3=Drob(6,2)
# print(Drob.countobjects())
#
# class Convert:
#     count = 0
#     @staticmethod
#     def faren(x):
#         Convert.count += 1
#         return (x * (9 / 5)) + 32
#     @staticmethod
#     def Celsius(y):
#         Convert.count += 1
#         return (y - 32) * 5 / 9
#     @staticmethod
#     def countobjects():
#         return Convert.count
#
# res1 = Convert.faren(5)
# res2 = Convert.Celsius(res1)
# print(Convert.countobjects())

# class Con:
#     @staticmethod
#     def funt(x):
#         return round(x/2.205,2)
#     @staticmethod
#     def kg(y):
#         return round(y*2.205,2)
#     @staticmethod
#     def inch(z):
#         return round(z/39.37,2)
#     @staticmethod
#     def metr(f):
#         return round(f *39.37, 2)
# res1 = Con.funt(50)
# res2 = Con.kg(res1)
# res3 = Con.inch(100)
# res4 = Con.metr(res3)
# print(res1)
# print(res2)
# print(res3)
# print(res4)


