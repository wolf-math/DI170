class Person:
    def something(self):
        print("something")
    
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def age(self):
        return 2026 - self.birth_year
    
    def intro(self):
        return f"Hello there! My name is {self.name}"
    
joel = Person('Joel', 1991)

print(joel.name)
print(joel.intro())
print(joel.age())

# me = Person

# rabea = me()
# rabea.something()