shift = 5

fp = open("Challenge60.txt","r")
fpWrite = open("Challenge60Encrypted.txt","w")

sentence = fp.read()
encrypted = ""

# Only encrypted lowercase
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
fpWrite.write(encrypted)
