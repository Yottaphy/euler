import numpy as np
import math

def iteration(num):
    reverse = int(str(num)[::-1])
    return num + reverse

def isPalindrome(num):    
    reverse = int(str(num)[::-1])
    return num == reverse

lychrel = 0
for num in range(1,10001):
    counter = 1
    trial = num
    while counter <= 50:
        result = iteration(trial)
        if isPalindrome(result): break
        else:
            counter+=1
            trial = result
    if counter > 50:
        lychrel +=1

print(lychrel)