list = ['Toronto','Miami']
option = int(input("1.Add a travel destination\n2.Find a travel destination\n3.Remove a travel destination\n4.Sort destinations by alphabet\n5.Count destinations"))
if(option==1):
    destination = input("Enter the destination you want to add:")
    list.append(destination)
elif(option==2):
    search = input("Enter the destination you want to find:")
    print("Found at index: "+str(list.index(search)))
elif(option==3):
    remove = input("Enter the destination you want to remove")
    list.remove(remove)
elif(option==4):
    list.sort()
elif(option==5):
    print("List has "+str(len(list))+" destinations")
else:
    print("Invalid input")

print(list)
