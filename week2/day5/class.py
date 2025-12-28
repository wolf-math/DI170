# class Dog:
#     # Initializer / Instance Attributes
#     def __init__(self, name):
#         print("A new dog has been initialized!")
#         print(f"His name is {name}")
#         self.name = name

# my_dog = Dog('Peanut')
# gabes_dog = Dog('Jacob')

# print(my_dog.name)
# print(gabes_dog.name)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# first_person = Person("John", 36)

# print(first_person.name)
# print(first_person.age)

# second_person = Person("Billy", 64)

class Dog:
    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("Her name is", name_of_the_dog)
        self.name = name_of_the_dog

    def bark(self):
        print(f"{self.name} barks! Woof")

    def walk(self, number_of_meters):
        print(f"{self.name} walked {number_of_meters} meters")

    def rename(self, new_name):
        self.name = new_name

# peanut = Dog('Peanut')
# peanut.bark()
# peanut.walk(200)
# peanut.rename('Jelly')
# print(peanut.name)
# peanut.name = 'Peanut'
# print(peanut.name)


# my_str = "hello world"
# my_str.upper()

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Hello my name is " + self.name)

    def change_name(self, new_name):
        self.name = new_name
  

first_person = Person("John", 36)
first_person.show_details()
first_person.change_name('Aloicous')