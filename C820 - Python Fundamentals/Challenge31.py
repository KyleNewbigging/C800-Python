sentence = input("Enter a sentence to remove vowels from:")
vowels = ['a','e','i','o','u']
i = 0
while i < len(sentence):
    if sentence[i] in vowels:
        sentence = sentence.replace(sentence[i],"")
    i+=1
print(sentence)
