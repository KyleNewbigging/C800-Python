from CarClass import Car, Motorcycle, Truck

fObj = open("Challenge64.txt","r")
lines = fObj.readlines()
fObj.close()
print(lines)
list = []
i=0
while i < len(lines):
    make = lines[i][lines[i].index(": ")+2:].rstrip()
    i+=1
    print(make)
    model = lines[i][lines[i].index(": ")+2:].rstrip()
    i+=1
    year = int(lines[i][lines[i].index(": ")+2:].rstrip())
    i+=1
    price = int(lines[i][lines[i].index(": ")+2:].rstrip())
    i+=1
    used = bool(lines[i][lines[i].index(": ")+2:].rstrip())
    i+=1
    mileage = int(lines[i][lines[i].index(": ")+2:].rstrip())
    i+=1
    doors = int(lines[i][lines[i].index(": ")+2:].rstrip())
    i+=1
    available = bool(lines[i][lines[i].index(": ")+2:].rstrip())
    i+=1
    typeCheck = lines[i]
    if(typeCheck != "\n"):
        type = typeCheck[lines[i].index(": ")+2:].rstrip()
        i+=1
        bedSizeCheck = lines[i]
        if(bedSizeCheck != "\n"):
            bedSize = bedSizeCheck[lines[i].index(": ")+2:].rstrip()
            i+=1
            truck = Truck(make,model,year,price,used,mileage,doors,available,type,bedSize)
            list.append(truck)
        else:
            motorcycle = Motorcycle(make,model,year,price,used,mileage,doors,available,type)
            list.append(motorcycle)
    else:
        car = Car(make,model,year,price,used,mileage,doors,available)
        list.append(car)

    i+=1
    


#print(list)
option=0
while option!=4:
    option = int(input("Select one of the Options:\n1) Find a car\n2) Add a car\n3) Mark a car sold\n4) Exit\n"))
    if option == 1:
        model = input("Enter the cars model:")
        for x in list:
            if x.model == model:
                print(x.stringify())

    elif option == 2:
        make = input("Enter car's make:")
        model = input("Enter car's model:")
        year = int(input("Enter car's year:"))
        price = int(input("Enter the car's price:"))
        used = bool(input("Enter if the car is used:"))
        mileage = int(input("Enter the car's mileage:"))
        doors = int(input("How many doors does the car have:"))
        available = bool(input("Enter if the car is available:"))
        typeCheck = input("Car,Motorcycle, or Truck (c/m/t):")
        if typeCheck != "c":
            type = input("Enter the vehicle's type:")
            if typeCheck == "t":
                bedSize = input("Enter the truck's bed size:")
                truck = Truck(make,model,year,price,used,mileage,doors,available,type,bedSize)
                list.append(truck)
            else:
                motorcycle = Motorcycle(make,model,year,price,used,mileage,doors,available,type)
                list.append(motorcycle)
        else:
            car = Car(make,model,year,price,used,mileage,doors,available)
            list.append(car)

    elif option == 3:
        model = input("Enter the Model that sold:")
        for x in list:
            if x.model == model:
                x.available = False

    elif option == 4:
        print("Good bye")

    else:
        print("Invalid input!")

#write to file
fObj = open("Challenge64.txt","w")

for car in list:
    fObj.write(car.stringify()+"\n")
fObj.close()