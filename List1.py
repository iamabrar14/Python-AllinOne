#A list is an ordered, mutable (changeable), indexed collection that allows duplicate elements.
fruits = ['apple', 'banana', 'cherry']

# Indexing
print(fruits[0])  # apple

# Slicing
print(fruits[1:])  # ['banana', 'cherry']

# Append
fruits.append('orange')  # Adds to the end

# Insert
fruits.insert(1, 'kiwi')  # Insert at index 1

# Remove
fruits.remove('banana')  # Removes first occurrence

# Pop
last = fruits.pop()  # Removes and returns last element

# Loop through list
for fruit in fruits:
    print(fruit)

# List length
print(len(fruits))
# List Covered in Midterm Practice