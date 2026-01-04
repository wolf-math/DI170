# class Person:
#   def __init__(self, name, lastName):
#       self.name = name
#       self.lastName = lastName

#   def __repr__(self):
#       return f"{self.__class__.__name__} : {self.name} {self.lastName}"

#   def __add__(self, other):
#       return Person(self.name, other.lastName)

# father = Person('John', 'Snow')
# mother = Person('Kaleesi', 'MotherOfDragons')

# child = father + mother
# print(child)

# child2 = mother + father
# print(child2)


class Car:
    def __init__(self, color):
        self.color = color

    def __add__(self, other):
        if isinstance(other, Car):
            print("CRASH!!!")
            print(f"{self.color} + {other.color}")
            return None
        else:
            raise TypeError("Can only add Car to Car")

    
my_car = Car("green")
abdallah_car = Car("blue")

# added = my_car.add(abdallah_car)

added_again = my_car + abdallah_car