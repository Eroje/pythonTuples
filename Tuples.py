# Tuples in Python

# Conventionally, tuples look like this,

Fruit = ("Apples", 4, "Bananas", 5, "Oranges", 6) # Tuple

List_of_Fruit = ["Apples", 4, "Bananas", 5, "Oranges", 6] # List
print(type(List_of_Fruit))
# We can modify elements within a list. We can't modify elements within a tuple!
List_of_Fruit[0] = "Strawberries"
print(List_of_Fruit)

# We can perform similar operations on tuples and list
print(Fruit[1:5]) # Slice in tuple
print(Fruit[2]) # Recalling element within a tuple

# Concatenation of Tuples
Fruit = Fruit[0:4] + ("Cherries", 10)
print(Fruit)

# Tuples with one element Must have a comma otherwise python sees it as an integer
x = (5, )
print(type(x))

# Creating a tuple
another_tuple = tuple(("Hello", 18, True))
print(type(another_tuple))

# Converting a tuple to a list and back to tuple
Fruit = list(Fruit)
Fruit.append("Pears")
Fruit = tuple(Fruit)
print(Fruit)

# Unpacking tuples
Fruit = ("Apples", "Bananas", "Pears", "Oranges", "Strawberries")
(one, two, three, four, five) = Fruit
print(one)
print(two)
(one, two, *three) = Fruit
print(three) # Returns a list
print(tuple(three)) # back to tuple
(one, *two, three, four) = Fruit
print(two)

# Incorporate loops within tuples
for i in range(len(Fruit)):
    print(Fruit[i])

