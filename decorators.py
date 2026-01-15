from functools import wraps

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
        wraps(func)(self)  # Preserve metadata
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} called {self.count} times")
        return self.func(*args, **kwargs)

@CountCalls
def greet():
    print("Hello!")

greet()  # greet called 1 times
greet()  # greet called 2 times

@CountCalls
def say_hi():
    print("hi!")

say_hi()