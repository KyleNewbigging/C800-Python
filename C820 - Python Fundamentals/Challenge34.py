for bottles in range(99,0,-1):
    print(str(bottles)+" bottles of cola on the wall, "+str(bottles)+" of cola.")
    if(bottles-1!=0):
        print("Take one down and pass it along, "+str(bottles-1)+" bottles of cola on the wall.")
    else:
        print("No more bottles")

max = int(input("Enter a number to calculate the sum between 1 and your number:"))
sum=0
for count in range(0,max+1):
    sum=sum+count
    count-=1

print(sum)

sentence = input("Enter a sentence to remove vowels from:")
vowels = ('a','e','i','o','u')
for x in sentence:
    if x in vowels:
        sentence = sentence.replace(x,"")

print(sentence)


