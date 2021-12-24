lexi = []
for num in range(123456789,9876543211):
    if len(lexi) > 1E6: break
    stringnum = str(num)
    if len(stringnum) == 9:
        stringnum = '0' + stringnum
    for i in range(0,10):
        count = 0
        if not stringnum.count(str(i)) == 1: break
    else:
        print(num)
        lexi.append(num)

print(lexi[1E6-1])

