
fObj = open("Challenge53.txt")

lines = fObj.readlines()
correct = 0.0
total = float(len(lines))/2

for x in range(0,len(lines),2):
    answer = input(lines[x])
    if(answer.lower()==lines[x+1].rstrip().lower()):
        correct+=1

print(str(round((correct/total)*100,1))+"%")

fObj.close()
