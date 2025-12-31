# class Animal:
#     def __init__(self, type, number_legs, sound):
#         self.type = type
#         self.number_legs = number_legs
#         self.sound = sound

# class Dog(Animal):
#     def __init__(self, type, number_legs, sound, fetch_ball):
#         # super().__init__(type, number_legs, sound)
#         self.fetch_ball = fetch_ball

# class Cat(Animal):
#     def __init__(self, type, number_legs, sound, hours_of_sleep):
#         super().__init__(type, number_legs, sound)
#         self.hours_of_sleep = hours_of_sleep

# george = Dog('Dog', 4, 'Grrr', True)

# print(george.fetch_ball)
# print(george.sound) # AttributeError



class MyClass:
    def func(self):
        print("I'm being called from the Parent class")


class ChildClass(MyClass):
    def func(self):
        print("I'm actually being called from the Child class")
        print("But...")
        # Calling the `func()` method from the Parent class.
        super().func()

my_instance_2 = ChildClass()
my_instance_2.func()