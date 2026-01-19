
def default_values(a, lst=[]):

    lst.append(a)
    return lst


print(default_values(1))
print(default_values(2))
print(default_values(3))
print(default_values(4, [5,6,7]))