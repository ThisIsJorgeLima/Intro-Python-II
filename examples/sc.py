

# Create List Comprehensions

Names = ["Harold", "Estevan", "Larry", "Lahn", "Oliver"]

# Create a new list using a list of comprehensions that stores the first letter of every name in Names

new_name = [i[0] for i in Names]
print(new_name)

Ages = [10, 17, 22, 15, 30, 37, 9, 18]

# Create a new list using a list comprehension with only numbers in Ages that are between 15 and 30 inclusive.

new_ages = [i for i in Ages if i >= 15 and i <= 30]
new_ages2 = [i for i in Ages if i in range(15, 31)]
print(new_ages)
print(new_ages2)

# Create a LC to find names that end in n
names = [i for i Names if i[-1] == 'n']
print(names)
