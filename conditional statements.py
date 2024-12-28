# 1. Question: What will be the result of using an if statement to check if a number is positive?
a = 5
if a > 0:
    result = "Positive"
else:
    result = "Non-positive"
print("Result of if statement:", result)  # Output: Result of if statement: Positive
# Logic: The if statement checks if a is greater than 0.

# 2. Question: What happens when the if-else statement is used to check if a number is negative or positive?
a = -3
if a > 0:
    result = "Positive"
else:
    result = "Negative or Zero"
print("Result of if-else statement:", result)  # Output: Result of if-else statement: Negative or Zero
# Logic: The if-else statement checks if a is greater than 0 or not.

# 3. Question: How does the elif statement work for multiple conditions?
a = 10
if a < 5:
    result = "Less than 5"
elif a == 10:
    result = "Equal to 10"
else:
    result = "Greater than 5 but not 10"
print("Result of elif statement:", result)  # Output: Result of elif statement: Equal to 10
# Logic: The elif checks if a equals 10 when the first condition fails.

# 4. Question: How does the nested if statement work?
a = 10
if a > 0:
    if a % 2 == 0:
        result = "Even positive number"
    else:
        result = "Odd positive number"
else:
    result = "Non-positive number"
print("Result of nested if statement:", result)  # Output: Result of nested if statement: Even positive number
# Logic: The nested if checks if a is positive and even.

# 5. Question: What is the result of checking multiple conditions using logical AND in an if statement?
a = 5
b = 10
if a > 0 and b > 0:
    result = "Both are positive"
else:
    result = "At least one is non-positive"
print("Result of logical AND:", result)  # Output: Result of logical AND: Both are positive
# Logic: The and operator checks if both a and b are positive.

# 6. Question: What happens when using logical OR in an if statement?
a = -5
b = 10
if a > 0 or b > 0:
    result = "At least one is positive"
else:
    result = "Neither is positive"
print("Result of logical OR:", result)  # Output: Result of logical OR: At least one is positive
# Logic: The or operator checks if either a or b is positive.

# 7. Question: How does the not operator affect the condition in an if statement?
a = False
if not a:
    result = "a is False"
else:
    result = "a is True"
print("Result of not operator:", result)  # Output: Result of not operator: a is False
# Logic: The not operator inverts the boolean value of a.

# 8. Question: What happens when a condition is not met in an if-else statement?
a = 0
if a > 0:
    result = "Positive"
else:
    result = "Zero or Negative"
print("Result when condition is not met:", result)  # Output: Result when condition is not met: Zero or Negative
# Logic: The else block executes when the if condition fails.

# 9. Question: How does the if statement work with an equality check?
a = 15
if a == 15:
    result = "Equal to 15"
else:
    result = "Not equal to 15"
print("Result of equality check:", result)  # Output: Result of equality check: Equal to 15
# Logic: The if statement checks if a equals 15.

# 10. Question: What will happen if an if statement checks for inequality using !=?
a = 8
if a != 10:
    result = "Not equal to 10"
else:
    result = "Equal to 10"
print("Result of inequality check:", result)  # Output: Result of inequality check: Not equal to 10
# Logic: The != operator checks if a is not equal to 10.

# 11. Question: How does the if statement handle multiple conditions with nested logical operators?
a = 10
b = 20
if a < b and b > 15:
    result = "b is greater than a and 15"
else:
    result = "Condition not met"
print("Result of nested logical operators:", result)  # Output: Result of nested logical operators: b is greater than a and 15
# Logic: The if statement checks two conditions with and.

# 12. Question: What happens when you use a combination of elif and else?
a = 7
if a > 10:
    result = "Greater than 10"
elif a == 7:
    result = "Equal to 7"
else:
    result = "Less than 7"
print("Result of elif and else combination:", result)  # Output: Result of elif and else combination: Equal to 7
# Logic: The elif checks if a equals 7 after the first condition fails.

# 13. Question: How does the if statement handle comparisons with strings?
a = "apple"
if a == "apple":
    result = "It is an apple"
else:
    result = "It is not an apple"
print("Result of string comparison:", result)  # Output: Result of string comparison: It is an apple
# Logic: The if statement compares a with "apple".

# 14. Question: What will happen if a condition checks whether a value is in a list?
a = 3
if a in [1, 2, 3, 4, 5]:
    result = "a is in the list"
else:
    result = "a is not in the list"
print("Result of membership check:", result)  # Output: Result of membership check: a is in the list
# Logic: The if statement checks if a is present in the list.

# 15. Question: What happens when a condition checks whether a value is not in a list?
a = 6
if a not in [1, 2, 3, 4, 5]:
    result = "a is not in the list"
else:
    result = "a is in the list"
print("Result of not in check:", result)  # Output: Result of not in check: a is not in the list
# Logic: The not in operator checks if a is not present in the list.

# 16. Question: How does the if statement behave with a zero value in conditional expressions?
a = 0
if a:
    result = "Non-zero value"
else:
    result = "Zero"
print("Result of zero value check:", result)  # Output: Result of zero value check: Zero
# Logic: In Python, zero evaluates to False, so the else block is executed.

# 17. Question: What happens when a condition checks if a value is greater than or equal to another value?
a = 5
b = 10
if a >= b:
    result = "a is greater than or equal to b"
else:
    result = "a is less than b"
print("Result of greater than or equal check:", result)  # Output: Result of greater than or equal check: a is less than b
# Logic: The >= operator checks if a is greater than or equal to b.

# 18. Question: What happens when a condition checks for a value less than or equal to another value?
a = 4
b = 5
if a <= b:
    result = "a is less than or equal to b"
else:
    result = "a is greater than b"
print("Result of less than or equal check:", result)  # Output: Result of less than or equal check: a is less than or equal to b
# Logic: The <= operator checks if a is less than or equal to b.

# 19. Question: How does the if statement work with boolean conditions?
a = True
if a:
    result = "Condition is True"
else:
    result = "Condition is False"
print("Result of boolean condition:", result)  # Output: Result of boolean condition: Condition is True
# Logic: The if statement evaluates the boolean value of a.

# 20. Question: What happens when a condition is checked using a custom function return value?
def is_even(a):
    return a % 2 == 0

a = 8
if is_even(a):
    result = "a is even"
else:
    result = "a is odd"
print("Result of custom function check:", result)  # Output: Result of custom function check: a is even
# Logic: The if statement checks if the function returns True for even numbers.