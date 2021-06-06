from eulerfuncs import factorial

total = 0
num = str(factorial(100))
print(num)
for i in range(0,len(num)):
    total += int(num[i])
print(total)