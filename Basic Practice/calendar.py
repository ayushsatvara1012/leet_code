import calendar

def calendayFunc(y,m,d):
    aryCal = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
    weekday = calendar.weekday(y, m, d)
    return aryCal[weekday]

userInput = int(input())
values = userInput.split()
print(values)