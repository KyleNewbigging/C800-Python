
fOdd = open("Challenge55Odd.txt")
fEven = open("Challenge55Even.txt")

oddLines = fOdd.readlines()
evenLines = fEven.readlines()

oddIndex = 0
evenIndex = 0

for x in range(1,len(evenLines)+len(oddLines)+1):
    if x%2!=0:
        print(oddLines[oddIndex].rstrip()+" ",end="")
        oddIndex+=1
    else:
        print(evenLines[evenIndex].rstrip()+" ",end="")
        evenIndex+=1