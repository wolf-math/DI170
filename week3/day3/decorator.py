def add_one(num):
    return num + 1

@add_one
def double(num):
    return num * 2

ans = double(5)
print(ans)