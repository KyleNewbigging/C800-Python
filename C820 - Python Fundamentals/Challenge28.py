list = ['Milk','Eggs','Apples']
option = int(input("1.Add a grocery item\n2.Print the list\n3.Sort the list\n4.Remove an item\n5.Count destinations\n6.Replace item"))
if(option==1):
    item = input("Enter a grocery item you want to add:")
    list.append(item)
    list.sort()
elif(option==3):
    list.sort()
elif(option==4):
    remove = input("Enter the item you want to remove")
    list.remove(remove)
elif(option==5):
    print("List has "+str(len(list))+" items")
elif(option==6):
    replace = input("Enter the item to be replaced:")
    new = input("Enter the new item to replace "+replace+":")
    index = list.index(replace)
    list.remove(replace)
    list.insert(index,new)
else:
    print("Invalid input")

print(list)
