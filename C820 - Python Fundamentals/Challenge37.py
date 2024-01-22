shift = int(input("Enter shift value:"))
sentence = input("Enter a sentence you want encrypted:")
encrypted = ""
for i in range(len(sentence)):
    if sentence[i].islower():
        shifted = (ord(sentence[i])+shift)
        if shifted >= 123:
            encrypted += chr(shifted-26)
        else:
            encrypted += chr(shifted)
    else:
        encrypted += sentence[i]
print(encrypted)
