# Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it. And also it must return both addition and subtraction in a single return call

# For example:

# def calculation(a, b):
#     return (a-b, a+b)

# minus, plus = calculation(40, 10)
# print(minus, plus)

# print(calculation)

# def i_am_cool():
#     pass

# my_funcs = [calculation, i_am_cool]

# def function_function(list_of_funcs):
#     for func in list_of_funcs:
#         print(func)

# function_function(my_funcs)


def my_f1():
    print("Hello")

def my_f2():
    print("Word")

def my_f3():
    print("This is Rick!")

list_of_functions = [my_f1, my_f2, my_f3]

for function in list_of_functions:
    function()