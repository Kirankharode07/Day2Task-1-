# Square of numbers
numbers =[1,2,3]
square_dict = {num: num**2 for num in numbers}
print(square_dict)
# square
squares = {x: x **2 for x in range(6)}
print(squares)
# filter even numbers
even_squares = {x: x**2 for x in range(10) if  x % 2==0}
print(even_squares)

# convert keys to uppercase
data = {"name": "John", "city": "Paris"}
upper_keys = {key.upper(): value for key, value in data.items()}
print(upper_keys)

# create a dictionary from two list
keys = ["name","age", "city"]
values = ["John",25, "New York"]
person = {k: v for k, v in zip(keys, values)}
print(person)