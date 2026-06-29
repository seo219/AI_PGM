def addMany(*args):
    result = 0
    # print(type(args))
    for i in args:
        result += i
    return result

print(addMany(1,2))
print(addMany(1,2,3,4,5))
print(addMany(1,2,3,4,5,6,7,8,9,10))

dict1 = {"name":"Alice", "age":30, "city":"New York"}
dict2 = {"name":"Bob", "age":25, "city":"Los Angeles"}

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Charlie",age="20",city="a")