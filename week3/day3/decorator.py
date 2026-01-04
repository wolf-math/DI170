def add_one(func):
    def wrapper(num):
        return func(num) + 1
    return wrapper

@add_one
def double(num):
    return num * 2

ans = double(5)
print(ans)