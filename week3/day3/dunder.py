class Eden:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __str__(self):
        return f"Hello! my name is {self.name}"
    
    def __len__(self):
        return len(self.name)
    
    def __call__(self):
        return f"{self.name} is {self.height} cm tall."
    
    def __repr__(self):
        return f"{self.name} is a cool person"
    
my_friend = Eden('Eden', 190)
print(str(my_friend))
print(len(my_friend))
res = my_friend()
print(res)

print(my_friend)
