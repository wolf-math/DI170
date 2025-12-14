# Ask the user for a number between 1 and 100
user_num = int(input('pick a number between 1 and 100: '))
# If the number is divisible by both three and five, print FizzBuzz instead.
if user_num % 15 == 0:
    print('fizzbuzz')
# If the number is divisible by three, print Fizz
elif user_num % 3 == 0:
    print('fizz')
# If the number is divisible by five, print Buzz.
elif user_num % 5 == 0:
    print('buzz')