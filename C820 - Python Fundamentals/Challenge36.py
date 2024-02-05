import random

list = ["apple","baseball","water","queen","television","word","hangman","python","condition","ten"]
word = list[random.randint(0,len(list))]
print("The word is "+str(len(word))+" characters long")
for x in range(5):
    letter = input("Guess a letter in the word:")
    if letter in word:
        print(letter+" is in the word!")
    else:
        print(letter+" is NOT in the word")

guess = input("Guess what you think the word is:")
if guess==word:
    print("Congrats you guessed the word!")
else:
    print("Incorrect, the word was "+word)
