''' ControlWork'''

# 1. Инкапсуляция

class Person:
    def __init__(self):
        self._age = 0

    def set_age(self, age):
        if age < 0:
            print(f'Ошибка при вводе возраста!')
        else:
            self._age = age

    def get_age(self):
        return self._age

person = Person()
person.set_age(-20)
person.set_age(25)

print(person.get_age())


# 2. Наследование

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}: 'I am  an animal'")

class Dog(Animal):
    def speak(self):
        print(f"{self.name}: 'Woof' ")

class Cat(Animal):
    def speak(self):
        print(f"{self.name}: 'Meow'")


dog = Dog("Buddy")
cat = Cat("Kitty")

dog.speak()
cat.speak()


# 3. Полиморфизм

class Vehicle():
    def move(self):
        return 'Vehicle is moving'

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"

def move(vehicle):
    return vehicle.move()

car = Car()
bicycle = Bicycle()
print(move(car))
print(move(bicycle))

# 4.Абстракция

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle (width = {self.width}, height = {self.height})'

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f'Circle (radius = {self.radius})'

    def area(self):
        return round(3.1416 * self.radius ** 2, 2)


rectangle = Rectangle(10, 5)
#print(rectangle)
print(rectangle.area())

circle = Circle(7)
#print(circle)
print(circle.area())