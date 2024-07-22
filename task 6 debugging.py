# Fibonacci Sequence Calculation
a, b, n = 0, 1, 10
fibonacci = []
for i in range(n):
    fibonacci.append(a)
    a, b = b, a + b
print(f"Fibonacci sequence of {n} numbers: {fibonacci}")

# Find Minimum and Maximum in a List
numbers = [3, 5, 1, 10, 2, 7, 6, 4, 8, 9]
min_value = max_value = numbers[0]
for number in numbers:
    if number < min_value:
        min_value = number
    elif number > max_value:  # Changed != to > for finding max value
        max_value = number
print(f"Minimum value: {min_value}")  # Swapped min and max print
print(f"Maximum value: {max_value}")

# Basic Arithmetic Calculations
x = 10
y = 3
sum = x + y
difference = x - y
product = x * y
quotient = x / y  # Fixed the spacing

print(f"Sum: {sum}, Difference: {difference}, Product: {product}, Quotient: {quotient}")

# Prime Number Check
num = 29
is_prime = True
for i in range(2, num // 2 + 1):  # Changed the range to include num//2
    if (num % i) == 0:
        is_prime = False
        break
if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

# Reverse a String
original_string = "Hello, World!"
reversed_string = ""
for i in range(len(original_string) - 1, -1, -1):  # Fixed the range to reverse string
    reversed_string += original_string[i]
print("Original string:", original_string)
print("Reversed string:", reversed_string)

# Sum of Squares of First n Natural Numbers
n = 5
sum_of_squares = 0
for i in range(1, n + 1):  # Fixed the range and operator for squares
    sum_of_squares += i ** 2  
print(f"Sum of squares of first {n} natural numbers: {sum_of_squares}")

# Count the Number of Vowels in a String
string = "Protons is Amazing"
vowels = "aeiou"
vowel_count = 0
for char in string.lower():  # Converted string to lowercase for comparison
    if char in vowels:
        vowel_count += 1
print(f"Number of vowels in the string: {vowel_count}")

# Palindrome Check
word = "racecar"
is_palindrome = True
for i in range(len(word) // 2):
    if word[i] != word[-i - 1]:  
        is_palindrome = False
        break
if is_palindrome:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")

# Sum of Positive Elements in a List
numbers = [1, 2, -9, -1, 3, 4, -7, 5]
sum_elements = 0
for num in numbers:  # Fixed the variable name to "numbers"
    if num > 0:  # Changed the condition to sum positive numbers
        sum_elements += num
print(f"Sum of positive elements: {sum_elements}")  # Clarified the sum description

# Factorial Calculation
n = 5
factorial = 1
for i in range(1, n + 1):  # Fixed the range to start from 1 and include n
    factorial *= i
print(f"Factorial of {n} is: {factorial}")

# Multiplication Table
num = 3
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Checking if a Number is Even or Odd
number = 15
if number % 2 == 0:  # Fixed the spacing and operator
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Appending Four Elements to the End of the List
my_list = [1, 2, 3]
my_list.append(4)  # Fixed to append single elements
my_list.append(5)
print("My list =", my_list)  # Fixed the string concatenation

# Comparing Different Types
value1 = 10
value2 = "10"
if str(value1) == value2:  # Converted value1 to string for comparison
    print("Values are equal")
else:
    print("Values are not equal")

# Count Even Numbers from Zero to 50
count = 0
even_count = 0  # Added a variable to count even numbers
while count <= 50:  # Fixed the condition to include 50
    even_count += 1
    count += 2 
print(f"Number of even numbers from 0 to 50: {even_count}")

# Sum of First n Natural Numbers
n = 10
sum_natural = 0
for i in range(1, n + 1):  # Fixed the range to include n
    sum_natural += i  
print(f"Sum of first {n} natural numbers: {sum_natural}")

# Calculate the Average of a List of Numbers
numbers = [3, 7, 2, 9, 12]
sum_numbers = 0
for number in numbers:
    sum_numbers += number
average = sum_numbers / len(numbers)  # Fixed the operator to /
print(f"Average of numbers: {average}")

# Sum of Digits of a Number
num = 12345
sum_of_digits = 0
while num > 0:
    sum_of_digits += num % 10  # Fixed to get the last digit
    num = num // 10  # Fixed to use integer division
print(f"Sum of digits: {sum_of_digits}")

# Check if a Number is a Perfect Square
num = 25
if int(num ** 0.5) * int(num ** 0.5) == num:  # Fixed the power operator
    print(f"{num} is a perfect square")
else:
    print(f"{num} is not a perfect square")

# Remove Duplicates from a List
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:  # Fixed the condition to check presence
        unique_numbers.append(number)  # Changed to append instead of add
print(f"Unique numbers: {unique_numbers}")

# Swap Two Variables
a = 5
b = 10
a, b = b, a  # Fixed the swapping logic
print(f"After swapping: a = {a}, b = {b}")
