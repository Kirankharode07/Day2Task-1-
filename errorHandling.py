# basic
try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result:", result)
except ZeroDivisionError:
    print("you cannnot divide by zero.")
except ValueError:
    print("please enter a valid number.")

#  multiple excepts
try:
    with open("data.text") as f:
        content = f.read()
except FileNotFoundError:
    print("Filenot found. check the filename.")
except PermissionError:
    print("No permission to read this file.")
   
# else block(runs only if no error)
try:
    n = int(input("Enter a number: "))
except ValueError:
    print("Not a number!")
else:
    print("Square is", n * n)

# finally block
f =None
try:
    f = open("log.text", "w")
    f.write("Hello")
except OSError as e :
    print("File error:", e)
finally:
    if f:
        f.close()
# Raising an exception
def percentage(x):
    if not (0 <= x <= 100):
        raise ValueError("percentage must be between 0 and 100")
    return x / 100

print(percentage(75))   # 0.75
print(percentage(150))  # raises ValueError