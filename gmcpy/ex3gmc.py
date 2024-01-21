class Car:
  #  speed = 0

   # def accelerate(self):
    #    self.speed += 10

   # def brake(self):
    #    self.speed -= 10

    def __init__(self , color , brand):
        self.color = color
        self.brand = brand


#Mcar = Car()
#Mcar.accelerate()
#print(Mcar.speed)
#Mcar.brake()
#print(Mcar.speed)

car = Car("red","bmw")
car1 = Car("green","toyota")
print(car.color)




