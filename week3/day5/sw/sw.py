# Read file line by line

# with open("./week3/day5/sw/nameslist.txt", "r") as f:
#     for line in f:
#         print(line.strip())

# Read only the fifth line

# with open("./week3/day5/sw/nameslist.txt", "r") as f:
#     lines = f.readlines()
#     fifth_line = lines[4]  # index 4 is the 5th line
#     print(fifth_line)


# # Read first 5 chars

# with open("./week3/day5/sw/nameslist.txt", "r") as f:
#     first_five_chars = f.read(5)
#     print(first_five_chars)


# # Read the whole file and return it as a list of strings, then split each name into letters

# with open("./week3/day5/sw/nameslist.txt", "r") as f:
#     names = f.read().splitlines()
#     letters = [list(name) for name in names]
#     print(letters)


# # How many occurances?

# with open("./week3/day5/sw/nameslist.txt", "r") as f:
#     names = [line.strip() for line in f]

# count_darth = names.count("Darth")
# count_luke  = names.count("Luke")
# count_lea   = names.count("Lea")

# print("Darth:", count_darth)
# print("Luke :", count_luke)
# print("Lea  :", count_lea)


# # Append your first name at the end 

# with open("./week3/day5/sw/nameslist.txt", "a") as f:
#     f.write("\nMEEEEE!!!")


# # Append Skywalker to every Luke

with open("./week3/day5/sw/nameslist.txt", "r") as f:
    lines = [line.rstrip("\n") for line in f]

with open("./week3/day5/sw/nameslist.txt", "w") as f:
    for name in lines:
        if name == "Luke":
            f.write("Luke SkyWalker\n")
        else:
            f.write(name + "\n")
