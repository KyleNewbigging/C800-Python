
fOdd = open("Challenge61Odd.txt","w")
fEven = open("Challenge61Even.txt","w")

string = input("Enter a sentence to save:")

words = string.split()

for x in range(len(words)):
    if (x+1)%2!=0:
        fOdd.write(words[x]+"\n")
    else:
        fEven.write(words[x]+"\n")