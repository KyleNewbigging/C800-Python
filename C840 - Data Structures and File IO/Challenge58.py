
list = [["password",0],["security",0],["e-transfer",0],["accounts",0],["cards",0],["deposit",0],["branch",0]]
fObj = open("Challenge58.txt")
string = fObj.read()
fObj.close()

for word in string.split():
    for x in range(len(list)):
        if(list[x][0] in word.lower()):
            list[x][1] += 1

print(list)