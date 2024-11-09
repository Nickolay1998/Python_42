##1
##set1 = {"Movie", "Game","App","Play", 5, 8, 10, 11,21, 47,"Mobile","Phone"}
##set_l= list(set1)
####print(set_l)


import random
set_num = {5, 8, 10, 11,21, 47}
g = [random.randint(1,50) for i in range(20)]
setg = set(g)
##print(set_num)
##print(setg)
##print(max(setg&set_num))
##print(min(setg&set_num))
##print(sum(setg&set_num))
##
##print(max(setg|set_num))
##print(min(setg|set_num))
##print(sum(setg|set_num))
##
##print(max(setg.symmetric_difference(set_num)))
##print(min(setg.symmetric_difference(set_num)))
##print(sum(setg.symmetric_difference(set_num)))
##print(sorted(setg.symmetric_difference(set_num),reverse=True))

##4
##f = sorted(setg.symmetric_difference(set_num),reverse=True)
##print(''.join([str(f[i])  for i in range(len(f))]))  1 вариант

##print(''.join(list(map(lambda i: str(i), sorted(setg.symmetric_difference(set_num),reverse=True)))))   #2 вариант
