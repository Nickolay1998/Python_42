#1
##x,y,z = 3,2,1
##z,y,x = x,y,z
##print(x,y,z)
##Total
##123

##2
##x = '\'                   это зарезервированый символ
##print(len(x))
##print(x)
##total error
##x = '\"'
##print(x)
##total "

##3
##print([i for i in range(0,-2)])
####Total []
##print([i for i in range(-2,0)])
##[-2, -1]
##print([i for i in range(0,-2,-1)])
##[0, -1]

##4
##def fun(n):
##    s=''
##    for i in range(n):
##        s+='*'
##        yield s

##for x in fun(3):
##    print(x,end="")
##******

##for x in fun(3):
##    print(x)
##*
##**
##***
