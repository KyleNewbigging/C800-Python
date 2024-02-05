for bottles in range(99,0,-1):
    print(str(bottles)+" bottles of cola on the wall, "+str(bottles)+" of cola.")
    if(bottles-1!=0):
        print("Take one down and pass it along, "+str(bottles-1)+" bottles of cola on the wall.")
    else:
        print("No more bottles")
