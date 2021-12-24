import operator
items = open('59_nums.txt', 'r').read().split(',')

dic1 = {}
dic2 = {}
dic3 = {}
letters =           0

#found the password: 'exp' by trial and error assuming most frequent character is ' ' and second is 'e'.

for i in range(len(items)):
    if i % 3 == 0:
        letters += int(items[i])^101
        if dic1.get(items[i]) == None:
            dic1[items[i]] = 1
        else: 
            dic1[items[i]] += 1

    if i % 3 == 1:
        letters += int(items[i])^120
        if dic2.get(items[i]) == None:
            dic2[items[i]] = 1
        else: 
            dic2[items[i]] += 1

    if i % 3 == 2:  
        letters += int(items[i])^112
        if dic3.get(items[i]) == None:
            dic3[items[i]] = 1
        else: 
            dic3[items[i]] += 1

print(letters)