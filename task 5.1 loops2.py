
print("task 1")
#task1
fruits = ["apples", "bananas", "oranges"]

output = ""
# Loop through the list and create variables dynamically
for i in range (0,len(fruits)):
    output += fruits[i]
    if i == (len(fruits) - 2):
        output += " and "
    elif i != (len(fruits) - 1):
        output += ", "    
        
print(output)   

print("task2")
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = int(input("pls enter a non negative number"))
output_1= sorted_list.copy()


if len(sorted_list) < 4:
    print("Error: The list must contain at least 4 values.")

if x >= len(sorted_list)/2:
    print("pls enter a smaller number")


for i in range(0, x):
    del output_1[0]

    del output_1[-1]
    
print(output_1)


#task3
print("               ")
print("               ")
print("task 3")


t = [3, 6,9, 10]
result = []
sum= 0

for i in t:
    sum += i 
    result.append(sum)

print(result)

#task4

print("               ")
print("               ")
print("task 4")


out = ""
num = [1, 3, 6, 9, 10]

for i in range(len(num) - 1):
    if num[i] < num[i + 1]:
        continue
    else:
        out = "False"
        break
else:
    out = "True"

print(out)


import math
import math

# Initialize the list of points
points = []

# Read the first point
x = input("Enter the x part of the coordinate: ")
if x != "":
    y = input("Enter the y part of the coordinate: ")
    points.append((float(x), float(y)))

# Read the remaining points
while True:
    x = input("Enter the x part of the coordinate: (blank to quit): ")
    if x == "":
        break  # Exit the loop if the x-coordinate is blank
    y = input("Enter the y part of the coordinate: ")
    points.append((float(x), float(y)))

# Compute the perimeter
perimeter = 0
for i in range(len(points)):
    x1, y1 = points[i]
    x2, y2 = points[(i + 1) % len(points)]  # Wrap around to the first point
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    perimeter += distance

# Display the result
print(f"The perimeter of that polygon is {perimeter:.5f}")




















#task6

message = input("Enter the message to encode/decode: ")
shift = int(input("Enter the shift amount (positive for encoding, negative for decoding): "))


result = ""


for char in message:
    
    if 'A' <= char <= 'Z':
        
        result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    
    elif 'a' <= char <= 'z':
        
        result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    else:
        
        result += char

# Print the result
print("Encoded/Decoded message:", result)

