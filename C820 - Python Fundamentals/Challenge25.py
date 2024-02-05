import random
rand_num = random.randint(1,6)
print("Hello world")
guess = int(input("Enter a guess (1 to 5) (Hint: "+str(rand_num)+")"))
if(guess==rand_num):
    print("congrats!!!")
else:
    print("NOPE!")
