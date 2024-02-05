class Car:
    def __init__(self,make,model,year,price,used,mileage,doors,available):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.used = used
        self.mileage = mileage
        self._doors = doors
        self.available = available

    def setMileage(self,newMileage):
        self.mileage = newMileage

    def setAvailable(self,newAvailable):
        self.available = newAvailable

    def stringify(self):
        return "Make: "+self.make+"\nModel: "+self.model+"\nYear: "+str(self.year)+"\nPrice: "+str(self.price)+"\nUsed: "+str(self.used)+"\nMileage: "+str(self.mileage)+"\nDoors: "+str(self._doors)+"\nAvailable: "+str(self.available)+"\n"

class Motorcycle(Car):
    def __init__(self,make,model,year,price,used,mileage,doors,available,type):
        self.type = type
        Car.__init__(self,make,model,year,price,used,mileage,doors,available)

    def stringify(self):
        return Car.stringify(self) +"Type: "+self.type+"\n"


class Truck(Car):
    def __init__(self,make,model,year,price,used,mileage,doors,available,type,bedSize):
        self.type = type
        self.bedSize = bedSize
        Car.__init__(self,make,model,year,price,used,mileage,doors,available)
    
    def stringify(self):
        return Car.stringify(self) +"Type: "+self.type+"\nBed Size: "+self.bedSize+"\n"