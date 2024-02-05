animals = {'hippo':'calf',
           "horse":"foal",
           "dog":"pup",
           "kangaroo":"joey",
           "monkey":"infant",
           "owl":"owlet",
           "parrot":"chick",
           "rabbit":"bunny",
           "rat":"pup",
           "cow":"calf",
           "skunk":"kit",
           "sheep":"lamb"}
option=1
while (option==1 or option==2 or option==3 or option==4):
    option = int(input("Select one of the options:\n1. Lookup animal babies\n2. Add animal and baby\n3. Delete animal and baby\n4. Print list"))
    if option == 1:
        animal = input("Enter an animal that you want it's baby's name:")
        if animal in animals:
            print("The baby name for "+animal+" is "+animals[animal])
        else:
            print(animal+" is not in the list")
    elif option == 2:
        animal = input("Enter an animal that you want to add:")
        baby = input("What is a baby "+animal+" called?")
        animals[animal] = baby
        print("added to the list")
    elif option == 3:
        animal = input("Enter an animal that you want to delete:")
        del animals[animal]
    elif option == 4:
        print(animals)

print("Good bye!")

        
