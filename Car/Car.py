# Klasy i obiekty


class Car:
    color = "any"
    engine = "some"
    weight = 1
    model = ""
    speed = 1
    # prywatna zmienna na sposob pythona
    __someNumber = 1

    def ride(self):
        ride = 'brr' * self.speed
        print(ride)

    def accelerate(self, newSpeed):
        self.speed = self.speed + newSpeed
        return self.speed

    def checkColor(self):
        print(self.color)

    def checkModel(self):
        print(self.model)

    def checkEngine(self):
        print(self.engine)

    def setModel(self, newModel):
        self.model = newModel
        return self.model

    def setColor(self, newCModel):
        self.color = newCModel
        return Car.color

    # konstruktor
    # method overloading on model variable
    def __init__(self, color, model=None):


        if model is not None:
            self.model = model
        else:
            self.model = "cheapest"

        self.color = color

        print('Car model is ' + self.model)
        print('Car color is ' + color)


class Bike():
    color = "green"

    def __init__(self, color, model=None):
        pass


# # stworzenie obiektu gdy nie ma konstruktora
# Car1 = Car()
# wywolanie konstruktora
# Car('red',"opel")


class Tesla(Car):
    engine = 'electric'

    # Method overiding
    def accelerate(self, newSpeed):
        self.speed = self.speed + newSpeed + 1
        return self.speed


class Opel(Car):
    engine = 'diesel'


# print(Car.color)
# print(Tesla.engine)
# print(Opel.engine)
# example with overloaded constructor method
Tesla1 = Tesla('red', "x")
Opel1 = Opel('black', 'astra')
Tesla2 = Tesla('black')
print(Tesla1.engine)
print(Opel1.engine)

# racing time
Tesla1.ride()
Opel1.ride()

Tesla1.accelerate(1)
Opel1.accelerate(1)

Tesla1.ride()
Opel1.ride()

Tesla1.setColor("blue")
Tesla1.checkColor()
print(Tesla1.color)
Tesla1.color = 'red'
print(Tesla1.color)
# print(Tesla1.__someNumber)
Bike1 = Bike

print(Bike.color)
# Bike.setColor("red")
