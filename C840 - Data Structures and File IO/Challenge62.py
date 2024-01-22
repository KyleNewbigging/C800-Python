fread = open("Challenge62.txt","r")

lines = fread.readlines()
fread.close()

animals = {}

for line in lines:
    parent = line[0:line.index(":")].rstrip()
    print(parent)
    baby = line[line.index(":")+1:len(lines)-1].rstrip()
    print(baby)
    animals[parent]=baby


option=1
while (option==1 or option==2 or option==3 or option==4):
    option = int(input("Select one of the options:\n1. Lookup animal babies\n2. Add animal and baby\n3. Delete animal and baby\n4. Print list\n"))
    if option == 1:
        animal = input("Enter an animal that you want it's baby's name:")
        if animal in animals:
            print("The baby name for "+animal+" is "+animals[animal])
        else:
            print(animal+" is not in the list")
    elif option == 2:
        animal = input("Enter an animal that you want to add:")
        baby = input("What is a baby "+animal+" called?\n")
        animals[animal] = baby
        print("added to the list")
    elif option == 3:
        animal = input("Enter an animal that you want to delete:")
        del animals[animal]
    elif option == 4:
        print(animals)

fwrite = open("Challenge62.txt","w")

for x in animals:
    fwrite.write(x+":"+animals[x]+"\n")

fwrite.close()
print("Saved!")

        
