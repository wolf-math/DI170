class MyClass:
  __counter = 0

  @classmethod
  def add(cls,a): 
    cls.__counter = cls.__counter + a
  
  @classmethod
  def access_count(cls):
    return cls.__counter

MyClass.add(3)


# new_class = MyClass()
# new_class.__counter = 1

# print(new_class.add(3))

# eden = MyClass()
# print(eden.__counter)

print(MyClass.access_count())