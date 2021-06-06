def isLeap(year):
    if year%400==0: return True
    if year%100==0: return False
    if year%4  ==0: return True
    return False

def daysSince(day,month,year):
    days = 0
    for i in range(1900,year):
        days+=365
        if isLeap(i): days +=1
    monthdays = {1: 31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    for i in range(1,month):
        days += monthdays[i]
    if isLeap(year) and month>2: days+=1
    days+= day
    return days

def isSunday(day,month,year):
    if daysSince(day,month,year) % 7 == 0: return True
    return False

total = 0
for y in range(1901,2001):
    for m in range(1,13):
        if isSunday(1,m,y): total+=1
    
print(total)

