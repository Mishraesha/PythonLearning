class Car:

    wheels = 4
    def __init__(self):
        self.mil=10
        self.com="Maruti"

car1 = Car()
car2 = Car()
Car.wheels=2
car1.wheels=3

car2.com="BMW"
car2.mil = 9
print(car1.wheels,car1.com,car1.mil)
print(car2.wheels,car2.com,car2.mil)