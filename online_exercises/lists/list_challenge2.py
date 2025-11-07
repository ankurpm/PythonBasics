'''
List Slicing and Iteration (Intermediate)
Use the list of cities: ['New York', 'London', 'Paris', 'Tokyo', 'Sydney', 'Rome'].
a.Create a new list called european_cities that contains only the cities from index 1 up to (but not including) index 5, using slicing.
b.Iterate through the original city list and print each city name along with its index (e.g., "City 0: New York").
'''
# Original list of cities
cities = ['New York', 'London', 'Paris', 'Tokyo', 'Sydney', 'Rome']

# a. Create a new list using slicing (index 1 up to but not including 5)
european_cities = cities[1:5]
print("European cities:", european_cities)

# b. Iterate through the list and print city name with index
for index, city in enumerate(cities):
    print(f"City {index}: {city}")
