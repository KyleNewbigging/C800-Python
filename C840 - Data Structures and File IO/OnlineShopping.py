from ShoppingCartClass import ShoppingCart, Grocery
storeInventory = []
apple = Grocery("Apple",10,0)
storeInventory.append(apple)
banana = Grocery("Banana",5,1)
storeInventory.append(banana)
carrot = Grocery("Carrot",25,2)
storeInventory.append(carrot)

print("Welcome to Kyle's Online Store:")
cart = ShoppingCart()
option=0
while option!=4:
    option = int(input("Select one of the Options:\n1) Add item to cart\n2) Remove item from cart\n3) Display cart\n4) Checkout (exit)\n"))
    if option == 1: # Add item to cart
        for x in storeInventory:
            print(x.stringify())
        name = input("Enter the name of food you want:")
        for x in storeInventory:
            if x.name == name:
                print(x.stringify())
                cart.addItem(x)

    elif option == 2: # remove item from cart
        for x in cart.itemList:
            print(x.stringify())
        name = input("Enter the name of the food to remove")
        remove = False
        for x in cart.itemList:
            if not remove and x.name == name:
                remove = True
                cart.removeItem(x)
        

    elif option == 3:
        print(cart.stringify())
        print("List:")
        for x in cart.itemList:
            print(x.stringify())

    elif option == 4:
        print("List:")
        for x in cart.itemList:
            print(x.stringify())
        print(cart.stringify())
        print("Good bye!")

    else:
        print("Invalid input!")