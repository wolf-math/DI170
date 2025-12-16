# password = ''
# while password != 'hello-world-123':
#   password = input('What is the top secret password? ')

# print('You guessed the right password!')

# while True: 
#     city = input("Please enter the name of a city you have visited (enter 'quit'  when you are finished): ")
#     if city == 'quit':
#         break
#     else:
#         print("I'd love to go to", city)

# print("Goodbye !")

current = 0
while current <= 10:
    current += 1
    if 3 < current < 7:
        continue
    print(current)