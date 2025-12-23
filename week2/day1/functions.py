# def say_hello():
#     """A function that says hello"""
#     print("Hello!") 

# say_hello()
# say_hello()
# say_hello()
# say_hello()


# def say_hello(username):
#     print(f"Hello {username}")

# say_hello('Bill')
# say_hello('Philip')
# say_hello('Matvey')
# say_hello('Dan')

# def say_hello(username, language="EN"):
#     if language == "EN":
#         print("Hello "+username)
#     elif language == "FR":
#         print("Bonjour "+username)
#     else:
#         print("This language is not supported: " + language)

# say_hello('Philip', 'FR')
# say_hello('Rabea')
# say_hello(username='Tom Sawyer')

# say_hello(input('name? '), input('language? '))

# say_hello(username="Rick", language="FR")
# say_hello(language="FR", username="Rick")
# say_hello(lang="FR", user="Rick")


# my_number = 4

# def numberator(number):
#     new_number = my_number * number # local scope
#     new_new_number = new_number + 8
#     # return f'{my_number} times {number} is {new_number}'
#     return new_number

# my_val = numberator(9)
# print(my_val * 8)

# my_number - 9




# def i_am_cool():
#     pass

# my_funcs = [calculation, i_am_cool]

# def function_function(list_of_funcs):
#     for func in list_of_funcs:
#         print(func)

# function_function(my_funcs)


# def my_f1():
#     print("Hello")

# def my_f2():
#     print("Word")

# def my_f3():
#     print("This is Rick!")

# list_of_functions = [my_f1, my_f2, my_f3]

# for function in list_of_functions:
#     function()


# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] 
# completed_models = []

# # Simulate printing each design until none are left. 
# # Move each design to completed_models after printing. 

# while len(unprinted_designs) != 0:    
#     current_design = unprinted_designs.pop() 

#     # Simulate creating a 3D print from the design.    
#     print("Printing model: " + current_design)    
#     completed_models.append(current_design)    

# # Display all completed models. 
# print("\nThe following models have been printed:") 
# for completed_model in completed_models:    
#     print(completed_model)

def print_models(unprinted_designs, completed_models):
    """    
    Simulate printing each design until none are left.    
    Move each design to completed_models after printing.    
    """

    while unprinted_designs:        
        current_design = unprinted_designs.pop()            

        # Simulate creating a 3D print from the design.        
        print("Printing model: " + current_design)        
        completed_models.append(current_design)        

def show_completed_models(completed_models):    
    """
    Show all the models that were printed.
    """    
    print("\nThe following models have been printed:")   
    for completed_model in completed_models:        
        print(completed_model)        

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] 
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

unprinted_designs = ['Starship Entiprise', '5 shekel shopping cart thingy']

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)