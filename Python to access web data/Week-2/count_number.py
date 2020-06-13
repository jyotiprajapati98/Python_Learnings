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
