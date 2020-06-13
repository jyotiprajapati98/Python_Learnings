"""Actual data: http://py4e-data.dr-chuck.net/regex_sum_456379.txt (There are 72 values and the sum ends with 805)
"""
#code here 
import re
handle = open('regex_sum_456379.txt')
sumAll = 0
for line in handle:
    line = line.rstrip()
    sumAll = numbers + sum(map(lambda x: int(x), re.findall('([0-9]+)', line)))

print(sumAll)

#method 2

import re
file=raw_input("enter file name")
hand = open(file)
x=list()
for line in hand:
     y = re.findall('[0-9]+',line)
     x = x+y

sum=0
for z in x:
    sum = sum + int(z)

print(sum)
