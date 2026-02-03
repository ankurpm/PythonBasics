#add function takes three positions arguments
def add(a, b, c):
    print(a)
    return a + b + c

#wrapper function takes variable position arguments
def wrapper(*args):
    print("Received:", args)
    #print(type(args))
    return add(*args)

print(wrapper(1, 2, 3))
