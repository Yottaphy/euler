from decimal import *
import time
import sys

def maxValue(lista):
    maxLen = 0
    empate = 0
    for tup in lista:
        if tup[1] == maxLen:
            empate += 1
        if tup[1] > maxLen:
            maxLen = tup[1]
            res = tup
    return res, empate

start = time.time()
getcontext().prec = 1000
getcontext().rounding = ROUND_DOWN
resList = []

diff = 0
for i in range(2, 1001):
    num = Decimal(1) / Decimal(i)
    for j in range(1, 1200):
        done = False
        a = Decimal(num*10**j)
        if not a == Decimal(int(a)):
            for k in range(j-1, 0, -1):
                b = Decimal(num*10**k)
                if Decimal(str(b)[:-(j-k)]) - Decimal(str(a)) == Decimal(int(Decimal(str(b)[:-(j-k)]) - Decimal(str(a)) )):
                    res = (i, j - k)
                    resList.append(res)
                    done = True
                    break
        if done:
            break
print(maxValue(resList))

end = time.time()

print(end-start)