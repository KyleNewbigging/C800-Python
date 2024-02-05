def stringToList(string,reverse=False):
    list = []
    for x in range(len(string)):
        if(reverse):
            list.append(string[len(string)-1-x])
        else:
            list.append(string[x])
    return list

print(stringToList("Hello world",True))