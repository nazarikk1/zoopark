from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self):
        pass

    def get_info(self):
        print(f"ім'я: {self.name}, вік: {self.age}")

class Dog(Animal):
    def make_sound(self):
        print("гав-гав!")

class Cat(Animal):
    def make_sound(self):
        print("няв-няв!")

class Parrot(Animal):
    def make_sound(self):
        print("привіт!")

dog = Dog(name="догггг", age=6)
cat = Cat(name="кітттт", age=4)
parrot = Parrot(name="перроттт", age=2)

dog.get_info()
dog.make_sound()

cat.get_info()
cat.make_sound()

parrot.get_info()
parrot.make_sound()
