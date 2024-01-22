def speedCheck(x):
    if x < 70:
        print("Ok")
    else:
        points = int((x - 70)/5)
        if points > 12:
            print("License Suspended!")
        else:
            print("Points: "+str(points))
speedCheck(98)
