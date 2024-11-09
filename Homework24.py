##import time
##def decoratortime(func):
##    def wrapper(*args, **kwargs):
##        start_time = time.time()  
##        result = func(*args, **kwargs)
##        end_time = time.time()  
##        totaltime = end_time - start_time
##        print(f"{totaltime} секунд")
##        return result
##    return wrapper
##
##
##@decoratortime
##def nums(x,diapazon):
##    listnums = []
##    for i in range(2, x,diapazon):
##        for j in range(2, int(i ** 0.5) + 1):
##            if i % j == 0:
##                break
##        else:
##            listnums.append(i)
##    return listnums
##print(nums(1000,7))

##def report(x,y):
##    report = f"Звіт\nПрибуток {x} грн\nВитрати {y} грн"
##    return report
##def ministry_of_finance(report):
##    def wrapper(x,y):
##        с = report(x,y)
##        state_institution = "   Міністерство фінансів\n"
##        return state_institution + с
##    return wrapper
##
##def tax_service(report):
##    def wrapper(x,y):
##        с = report(x,y)
##        state_institution = "   Податкова служба\n"
##        return state_institution + с
##    return wrapper
##
##@ministry_of_finance
##def finance_report(x,y):
##    return report(x,y)
##
##@tax_service
##def tax_report(x,y):
##    return report(x,y)
##print(finance_report(5000,3000))
##print(tax_report(5000,3000))








