class ShoppingCart:
    def __init__(self):
        self.numberOfItems = 0
        self.itemList = []
        self.totalPrice = 0

    def addItem(self,item):
        self.numberOfItems += 1
        self.itemList.append(item)
        self.totalPrice += item.price

    def removeItem(self,item):
        self.numberOfItems -= 1
        self.itemList.remove(item)
        self.totalPrice -= item.price

    def stringify(self):
        return "Num of Items: "+str(self.numberOfItems)+"\nTotal Price:"+str(self.totalPrice)+"\n" #List: "+str(self.itemList).strip("[]")+"\n"

class Grocery:
    def __init__(self,name,price,id):
        self.name = name
        self.price = price
        self.id = id

    def stringify(self):
        return "Name: "+self.name+"\nPrice: "+str(self.price)+"\nId:"+str(self.id)+"\n"

