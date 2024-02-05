
fObj = open("Challenge56.txt")
lines = fObj.readlines()

shift = int(lines[0].strip())
sentence = lines[1].lower()
encrypted = ""

for i in sentence:
    if i.islower():
        shifted = (ord(i)-shift)
        if shifted < 97:
            encrypted += chr(shifted+26)
        else:
            encrypted += chr(shifted)
    else:
        encrypted += i
print(encrypted)



