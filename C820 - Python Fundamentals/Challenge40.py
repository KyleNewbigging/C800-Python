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

animal = input("Enter an animal that you want it's baby's name:")
if animal in animals:
    print("The baby name for "+animal+" is "+animals[animal])
else:
    print(animal+" is not in the list")
    option = input("Would you like to add an entry for "+animal+" (yes or no):")
    if option == 'yes':
        baby = input("What is a baby "+animal+" called?")
        animals[animal] = baby
        print(animals)
        
