1.	List Comprehension

List comprehension is a short and cleaner way to create a new list in Python by applying some logic to an existing sequence

Instead of writing a loop and applying items one  by one, you can write everything in one line
Example:
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(squares)
output:
[1, 4, 9, 16, 25]

Syntax:
[expression for item in iterable if condition]
expression → What you want to store in the list.
item → Variable that takes each value from the iterable.
iterable → Something you loop through (like list, range, string).
if condition (optional) → Filter items.

2.Dict Comprehenssion
Dictionary comprehension is a short and cleaner way to create a dictionary in Python by applying some logic to an existing sequence
Instead of writing a loop and adding key-value pairs one by one, you can do it in one line
Example:

numbers = [1, 2, 3]
square_dict = {num: num ** 2 for num in numbers}
(square_dict)
Output:
{1: 1, 2: 4, 3: 9}


Syntax: {key_expression: value_expression for item in iterable if condition}
key_expression → What you want to use as the dictionary key.
value_expression → What you want to store as the dictionary value.
item → Variable for each element from the iterable.
iterable → Something you loop through.
 if condition (optional) → Filter items.
2.Error Handling in Python

An exception is how Python signals that something went wrong while running your code (e.g., dividing by zero, opening a missing file, converting bad input).

When an exception happens and you don’t handle it, Python stops your program and shows a traceback (error message + where it happened).

1.try-except
      Use to handle errors,so your program don’t crash


Example:
try:
  x = int(input("Enter a number: "))
     result = 10 / x
    print("Result:", result)
except ZeroDivisionError:
   print("You cannot divide by zero.")
except ValueError:
   print("Please enter a valid number.")

Code in try: runs first.
  If a matching except is found, it runs and the program continues.
2.Catching several exceptions in one line

try:
    risky()
except (ValueError, TypeError) as e:
    print("Invalid value or type:", e)



3. The finally block (always runs) try, except, else and finally Blocks

try Block:  lets us test a block of code for errors. Python will "try" to execute the code in this block. If an exception occurs, execution will immediately jump to the except block.
except Block:  enables us to handle the error or exception. If the code inside the try block throws an error, Python jumps to the except block and executes it. We can handle specific exceptions or use a general except to catch all exceptions.
else Block:  is optional and if included, must follow all except blocks. The else block runs only if no exceptions are raised in the try block. This is useful for code that should execute if the try block succeeds.
finally Block:  always runs, regardless of whether an exception occurred or not. It is typically used for cleanup operations (closing files, releasing resources).

5. file handling in python
  1)  Opening a file
                file = open("example.txt", "r")  # open for reading

Syntax:
              open(filename, mode)

Common modes:
Mode	  Meaning
"r"	  Read (default). File must exist.
"w"	Write (creates/overwrites file).
"a"	Append (adds to end).
"x"	Create new file, fail if exists.
"b"	Binary mode (add to above, e.g., "rb").
"t"	Text mode (default).

 File object methods
Method	What it does
.read(size)	Reads size characters (or whole file if no size).
.readline()	Reads one line.
.readlines()	Reads all lines into a list.
.write(string)	Writes a string.
.writelines(list)	Writes a list of strings.
.seek(pos)	Moves file pointer to position.
.tell()	Returns current position.
.close()	Closes file.
Common errors
FileNotFoundError → File doesn’t exist when reading.
PermissionError → No rights to open file.
Always close files or use with to avoid resource leaks.

1. Follow a Style Guide
Most companies follow an official style guide:
Python: PEP 8
JavaScript/TypeScript: Airbnb Style Guide, Google JS Guide, ESLint rules
Java: Google Java Style, Oracle Code Conventions
C#: Microsoft C# Coding Conventions
Why: Consistency → easier to read, maintain, and debug.

2. Naming Conventions
Variables: snake_case in Python, camelCase in JS/Java/C#
Constants: UPPER_CASE
Classes: PascalCase
Functions: snake_case (Python), camelCase (JS/Java)
Avoid: meaningless names like a, data1, temp2
*Snake_case - a naming convention where spaces in a phrase are replaced with underscores (_) and all letters are lowercase
*PascalCase-a naming convention where the first letter of each word in a compound word is capitalized, with no spaces, underscores, or dashes between the words

3. Code Structure & Organization
Keep functions short (ideally under 30 lines).
Each file/module should have a clear purpose.
Group related code into packages/modules.
Avoid deep nesting; use early returns.

4. Comments & Documentation
Docstrings for functions, classes, and modules.
Explain why, not just what.
Keep comments up to date.

5. Indentation & Spacing
Use consistent indentation (4 spaces in Python).
Space around operators and after commas:

6. Error Handling
Handle predictable errors with try-except (or equivalent).
Don’t swallow exceptions silently.
Log errors with meaningful messages.

7. Version Control Practices
Use Git (almost universal in industry).
Write clear commit messages:
Branch naming:
feature/add-user-auth
bugfix/fix-payment-error

8. Code Reviews
All production code should be reviewed by at least one teammate.
Be open to feedback.
•	Focus on readability, maintainability, and correctness.

9. Testing
Write unit tests for critical code.
Use frameworks: pytest (Python), JUnit (Java), Jest (JS).
Follow TDD (Test-Driven Development) where applicable.

10. Security Practices
Validate all inputs.
Avoid hardcoding passwords, keys, secrets → use environment variables.
Sanitize data before database queries (to prevent SQL Injection).
Use HTTPS and secure APIs.

11. Performance Considerations
Avoid unnecessary computations in loops.
Use efficient data structures (dict/set in Python instead of list for lookups).
Profile before optimizing.

