
filevar = open("mbox-short.txt", "r")#mbox-short.txt is a file name

count = 0
for line in filevar:
    print(line.strip())
    count = count + 1

print(count,"Lines")
