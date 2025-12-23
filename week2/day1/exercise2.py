people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

# Using map and filter, try to say hello to everyone who's name is less than or equal to 4 letters

filtered_list = list(filter(lambda name: len(name) <= 4, people))
print(filtered_list)

mapped = list(map(lambda name: f"hello {name}", filtered_list))
print(mapped)