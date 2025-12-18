my_books = {
  "title": "Harry Potter",
  "author": "JK Rowling",
  "chapter": 11,
  "publish date": 1999,
  "page": 420
}

# for key, value in my_books.items():
#     print(f"the {key} is {value}")

# for item in enumerate('abcd'):
#     print(item)

# for (index_count, letter) in enumerate('abcd'):
#     print(f'At index {index_count} the letter is {letter}')

# while True:
#     s = input('Enter something : ')
#     if s == 'quit':
#         break
#     print('Length of the string is', len(s))
# print('Done')

# from time import sleep

# a = 0
# while True:
#     a += 1
#     if a % 3 == 0:
#         continue
#     print(a)
#     sleep(2)

my_number = '1123478'

my_list = [int(num)**2 for num in my_number]
print(my_list)
