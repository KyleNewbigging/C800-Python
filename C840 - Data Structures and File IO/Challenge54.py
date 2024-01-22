
fObj = open("Challenge54.txt")

line = fObj.read()

for x in range(0,len(line),1):
    print(line[x],end="")

fObj.close()