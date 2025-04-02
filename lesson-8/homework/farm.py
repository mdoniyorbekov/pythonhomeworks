class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
    def make_sound(self):
        print(f"{self.name} is making a sound")
class Cow(Animal):
    def make_sound(self):
        print(f"{self.name} says Moooo")
    def produce_milk(self):
         print(f"{self.name} produces milk")
class Chicken(Animal):
    def make_sound(self):
        print(f"{self.name} says purr")
    def lay_egg(self):
        print(f"{self.name} lays an egg")
class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says meow")
    def drink_milk(self):
        print(f"{self.name} drinks milk")

if __name__== "__main__":
    cow = Cow("Masha", 5)
    chicken = Chicken("Purry", 2)
    cat = Cat("Tom", 3)

cow.eat()
cow.sleep()
cow.make_sound()

chicken.make_sound()
chicken.lay_egg()

cat.make_sound()
cat.drink_milk()
