'''
Basic Operations and Access (Beginner)

Create a list named `temperatures` storing the following daily high temperatures for a week: `[25, 28, 24, 26, 30, 27, 29]`.
    * Print the first temperature.
    * Print the last temperature using negative indexing.
    * Print the total number of days (the length of the list).
    * Change the temperature for the third day (index 2) to 22. Print the updated list.

'''
# Create a list of daily high temperatures
temperatures = [25, 28, 24, 26, 30, 27, 29]

# Print the first temperature
print("First temperature:", temperatures[0])

# Print the last temperature using negative indexing
print("Last temperature:", temperatures[-1])

# Print the total number of days
print("Total number of days:", len(temperatures))

# Change the temperature for the third day (index 2) to 22
temperatures[2] = 22

# Print the updated list
print("Updated temperatures:", temperatures)
