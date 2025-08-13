# squares of numbers
numbers = [1,2,3,4,5]
squares = [num ** 2 for num in numbers]
print(squares)
#creating list from 1-9
nums = [x for x in range(10)]
print(nums)
# convert words to uppercase
words =["apple","banana","cherry"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)

# using for loop:
cubes=[]
for x in range(10):
    if x % 2 ==0:
        cubes.append(x ** 3)
print("using for loop:",cubes)

# using list comprehension
easy = [x ** 3 for x in range(10) if x % 2 == 0]
print("using list comprehenssion:", easy)