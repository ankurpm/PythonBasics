'''
def calculate_sum(a, b):
    print(f'value of a is {a} and b is {b}')

calculate_sum(2, 1, )
'''
def calculate_area(length, width):
    print(f'length is {length}, width is {width}')
    return length * width

#calculate_area(width=200, length=100)

def print_values(a, b, /, *, c, d):
    print(f'values are {a} and {b} and {c} and {d}')

#print_values( 1,2,c =3,d = 4)

def default_values_function(a, b, c=1, d=4):
    print(f'values are {a} and {b} and {c} and {d}')

default_values_function(1, 2, 8)





