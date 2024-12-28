# Problem 1: Declare two variables and print their sum.
# Question: Write a program to declare two variables and calculate their sum.
# Example Input: a = 5, b = 10
# Example Output: 15
a = 5
b = 10
sum = a + b
print("Sum:", sum)

# Problem 2: Swap the values of two variables without using a third variable.
# Question: Swap the values of two variables without any additional variables.
# Example Input: a = 3, b = 7
# Example Output: a = 7, b = 3
a = 3
b = 7
a, b = b, a
print("a:", a, "b:", b)

# Problem 3: Assign the same value to three variables in a single line and print them.
# Question: Write a program to assign the same value to multiple variables in a single line.
# Example Input: a = b = c = 10
# Example Output: 10 10 10
a = b = c = 10
print(a, b, c)

# Problem 4: Calculate the area of a rectangle given length and breadth.
# Question: Write a program to calculate the area of a rectangle.
# Example Input: length = 5, breadth = 3
# Example Output: 15
length = 5
breadth = 3
area = length * breadth
print("Area of rectangle:", area)

# Problem 5: Declare a variable to store your name and print it.
# Question: Store and display your name using a variable.
# Example Input: name = "Alice"
# Example Output: Alice
name = "Alice"
print("Name:", name)

# Problem 6: Convert a given temperature from Celsius to Fahrenheit.
# Question: Write a program to convert Celsius to Fahrenheit.
# Example Input: celsius = 25
# Example Output: 77
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# Problem 7: Declare a variable for your age and check if you are eligible to vote.
# Question: Check if a person is eligible to vote based on their age.
# Example Input: age = 18
# Example Output: Eligible
age = 18
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# Problem 8: Calculate the simple interest for given principal, rate, and time.
# Question: Write a program to calculate simple interest.
# Example Input: principal = 1000, rate = 5, time = 2
# Example Output: 100
principal = 1000
rate = 5
time = 2
simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest)

# Problem 9: Assign a value to a variable and print its data type.
# Question: Determine and display the data type of a variable.
# Example Input: x = 10
# Example Output: <class 'int'>
x = 10
print("Data type:", type(x))

# Problem 10: Perform string concatenation using two variables.
# Question: Concatenate two strings stored in variables.
# Example Input: first = "Hello", second = "World"
# Example Output: HelloWorld
first = "Hello"
second = "World"
result = first + second
print("Concatenated string:", result)

# Problem 11: Declare a variable and check if it's even or odd.
# Question: Check whether a given number is even or odd.
# Example Input: num = 6
# Example Output: Even
num = 6
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Problem 12: Create a variable for the radius of a circle and calculate its area.
# Question: Calculate the area of a circle given its radius.
# Example Input: radius = 7
# Example Output: 153.94 (approx.)
radius = 7
area = 3.14159 * radius**2
print("Area of circle:", area)

# Problem 13: Calculate the perimeter of a square.
# Question: Write a program to calculate the perimeter of a square.
# Example Input: side = 4
# Example Output: 16
side = 4
perimeter = 4 * side
print("Perimeter of square:", perimeter)

# Problem 14: Find the square of a number.
# Question: Write a program to find the square of a number.
# Example Input: number = 6
# Example Output: 36
number = 6
square = number ** 2
print("Square of the number:", square)

# Problem 15: Calculate the area of a triangle.
# Question: Write a program to calculate the area of a triangle.
# Example Input: base = 6, height = 8
# Example Output: 24
base = 6
height = 8
area = (base * height) / 2
print("Area of triangle:", area)

# Problem 16: Find the cube of a number.
# Question: Write a program to find the cube of a number.
# Example Input: number = 3
# Example Output: 27
number = 3
cube = number ** 3
print("Cube of the number:", cube)

# Problem 17: Check if a number is positive, negative, or zero.
# Question: Write a program to check if a number is positive, negative, or zero.
# Example Input: number = -4
# Example Output: Negative
number = -4
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Problem 18: Find the remainder of a division.
# Question: Write a program to find the remainder when one number is divided by another.
# Example Input: dividend = 9, divisor = 4
# Example Output: 1
dividend = 9
divisor = 4
remainder = dividend % divisor
print("Remainder:", remainder)

# Problem 19: Find the average of three numbers.
# Question: Write a program to find the average of three numbers.
# Example Input: num1 = 4, num2 = 8, num3 = 12
# Example Output: 8.0
num1 = 4
num2 = 8
num3 = 12
average = (num1 + num2 + num3) / 3
print("Average:", average)

# Problem 20: Convert minutes to seconds.
# Question: Write a program to convert minutes to seconds.
# Example Input: minutes = 5
# Example Output: 300
minutes = 5
seconds = minutes * 60
print("Seconds:", seconds)
