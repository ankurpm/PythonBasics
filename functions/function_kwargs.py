
def my_function(**kwargs):
    print(kwargs)
    print(type(kwargs))

#print(my_function(a=1, b=2, c=3))

def print_user(**kwargs):
    print(kwargs)
    print(type(kwargs))
print(print_user(name="John", age=20))

