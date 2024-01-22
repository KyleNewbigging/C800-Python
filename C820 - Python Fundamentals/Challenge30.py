max = int(input("Enter a number to calculate the sum between 1 and your number:"))
sum=0
for count in range(0,max+1):
    sum=sum+count
    count-=1
    
print(sum)
