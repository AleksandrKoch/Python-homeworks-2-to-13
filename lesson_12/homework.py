# Homework: Classes
# Read carefully until the end before you start solving the exercises.

# Practice the Basics

# Basic Class

# - Create an empty class HouseForSale
# - Create two instances.
# - Add number_of_rooms and price as instance attributes.
# - Create print statements that show the attribute values for the instances.
class HouseForSale:
    pass

house1 = HouseForSale()
house2 = HouseForSale()
house1.number_of_rooms = 3
house1.price = 10
house2.number_of_rooms = 6
house2.price = 20

print(house1.number_of_rooms, house1.price)
print(house2.number_of_rooms, house2.price)
# ----------------------------------------------------------------------------------------------------------------------

# Instance Methods

# - Create a Computer class.
# - Create method:
#   - turn_on that prints Computer has Turned On
#   - turn_off that prints Computer has Turned Off
# - Create an instance of the Computer class then call each method.
class Computer:

    def turn_on(self):
        print("Computer has Turned On")

    def turn_off(self):
        print("Computer has Turned Off")

computer1 = Computer()

computer1.turn_on()
computer1.turn_off()

# ----------------------------------------------------------------------------------------------------------------------

# Constructor with Parameters

# - Create a Dog class.
# - Dog should have a constructor with a name parameter.
# - Dog should have a method say_name that prints the name of the dog.
class Dog:
    def __init__(self, name):
        self.name = name
    def say_name(self):
        print(self.name)

snoopy = Dog('Snoopy')
snoopy.say_name()
# ----------------------------------------------------------------------------------------------------------------------

# Inheritance

# Create the classes that would make the following code possible, with the caveat that
# both Dog and Cat must inherit from Animal.

class Animal:

    def __init__(self):
        pass

    def say_name(self):
        print("I do not have a name yet")

    def speak(self):
        print("I can't speak")

animal = Animal()
animal.say_name()   # Prints: I don't have a name yet.
animal.speak()      # Prints: I can't speak!

class Dog(Animal):
    def __init__(self, name):
        self.name = name
    def say_name(self):
        print(self.name)
    def speak(self):
        print("Woof")

dog = Dog('Fido')
dog.say_name()      # Prints: Fido
dog.speak()         # Prints: Woof!

class Cat(Animal):
    def __init__(self, name):
        self.name = name
    def say_name(self):
        print(self.name)
    def speak(self):
        print("Meow")

cat = Cat('Max')
cat.say_name()      # Prints: Max
cat.speak()         # Prints: Meow!
# ----------------------------------------------------------------------------------------------------------------------

# Exercises
# Exercise 1: Books and Authors

# Create an empty class called Book. Then create three instances.
# Add the following attributes for each of the instances: title, author, and publication_year.
# Create print statements to display the attributes of each one of the instances.

# Pre-code:
class Book:
   pass
#
book1 = Book()
book1.title = 'To Kill a Mockingbird'
book1.author = 'Harper Lee'
book1.publication_year = 1960

# Your code here
print(book1.title)
print(book1.author)
print(book1.publication_year)

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 2. Vehicle and Types of Vehicles

# Create a Vehicle class.
# - Its constructor should take the name and type of the vehicle and store them as instance attributes.
# - This Vehicle class should also have a show_type() instance method that prints out the
#   message: "<NAME_OF_VEHICLE> is a <TYPE_OF_VEHICLE>"
# - Create Car and Bike classes that inherit from Vehicle.
# - Create instances of Car and Bike and make them show their types.
class Vehicle:

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def show_type(self):
        print(f"{self.name} is a {self.type}")


class Car(Vehicle):
    pass


class Bike(Vehicle):
    pass

car = Car("Mustang", "Ford")
bike = Bike("Road King", "Harley Davidson")
car.show_type()
bike.show_type()
# ----------------------------------------------------------------------------------------------------------------------

# Exercise 3. Spot and correct the mistakes

# - You are given a task to create a Car class.
# - Each car will have attributes for model and year.
# - Unfortunately, the given code below contains several mistakes.
# - Your task is to find and correct these mistakes to make the code run successfully.
# - Please include a comment in the code explaining the corrections you made and why.

# Pre-code
class Car:
   def __init__(self, model, year): # self parameter was missing
       self.model = model # was self = model, missing dot and attribute name after self
       self.year = year # was year = year, missing self. reference before year attribute

my_car = Car("Toyota", 2025) # only one parameter "Toyota" was provided. Added another parameter "2025"
print(my_car.model) # no mistakes here
print(my_car.year) # no mistakes here

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 4. SmartHome with Constructor

# Create a SmartHome class that has a constructor __init__ and a send_notification() method.
#
# The constructor should initialize the attributes:
# - home_name
# - location
# - number_of_devices
class SmartHome:
    def __init__(self, home_name,location, number_of_devices):
        self.home_name = home_name
        self.location = location
        self.number_of_devices = number_of_devices
    # send_notification() should print a notification including the home_name and location.
    def send_notification(self, message="turn off the lights"): # message already added to the parameter list
        print(f"{message} {self.home_name} {self.location}")

# Create instances for the following:
# Home Name      Location      Number of Devices
# Villa Rosa     New York      15 devices
# Green House    California    10 devices
# Sea View       Florida       20 devices
home1 = SmartHome("Villa Rosa", "New York", "15 devices")
home2 = SmartHome("Green House", "California", "10 devices")
home3 = SmartHome("Sea View", "Florida", "20 devices")

# Call the send_notification() method for each instance,
home1.send_notification()
home2.send_notification()
home3.send_notification()

# passing a message reminding to turn off the lights.
home1.send_notification("Turn off the lights at")
home2.send_notification("Turn off the lights at")
home3.send_notification("Turn off the lights at")

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 5. Inheritance. Spot and correct mistakes

# You should have the following hierarchy of classes:

 # Animal
 # │
 # ├── Mammal
 # │
 # ├── Bird
 # │
 # └── Fish

# Each class has the following attributes:

# - Animal name
# - Mammal name, age, number of legs
# - Bird name, age, can fly or not
# - Fish name, age, number of fins

# But, the provided code for these classes and their instances has several mistakes
# related to hierarchy, class attributes, and instance creation.

# Find and correct these mistakes to make the code work properly.
# Leave a comment in the code explaining what the problems were and why it wouldn't work.
# There are seven mistakes in the pre-code.

# Pre-code
class Animal:
    def __init__(self, name): # class animal should have only one attribute - name, removing att age
        self.name = name # self and dot notation were missing, added them
        # age = age removed att age

class Mammal(Animal): # typo here Animals instead of Animal
    def __init__(self, name, age, num_legs):
        super().__init__(name) # removed age from super and added it bellow as this attribute is only in subclass
        self.age = age
        self.num_legs = num_legs

class Bird(Animal):
    def __init__(self, name, age, can_fly): #name and age parameters were missing
        super().__init__(name) # added parent constructor to inherit name attribute
        self.age = age # added age attribute
        self.can_fly = can_fly

class Fish(Animal): # fish should be a subclass of Animal instead of Mammal, changed Mammal to Animal
    def __init__(self, name, age, num_fins):
        super().__init__(name) # removed age parameter
        self.age = age # added age parameter
        self.num_fins = num_fins

tiger = Mammal('Tiger', 5, 4)
sparrow = Bird('Sparrow', 1, True) # parameter True is not enough here, need to also pass name 'Sparrow', age 1
goldfish = Fish('Goldfish', 2, 'Many')

