# (a) 
print("Hello World!")

# (b) 
user_name = input("Enter your name: ")
print("Welcome to Come and Die, " + user_name + "!")
x = "45"
y = 10
z = 2.5

# i. 
print(type(x))  # Output: <class 'str'>
print(type(y))  # Output: <class 'int'>
print(type(z))  # Output: <class 'float'>

# ii. 
x_as_int = int(x)
print(x_as_int + y)

# iii. 
print(y + z * 3)  # 10 + 7.5 = 17.5

# iv. 
print((y + z) * 3)  # (10 + 2.5) * 3 = 37.5

# v. 
y, z = z, y
print("Swapped values -> y:", y, "z:", z)

a = 5
b = 3

# Display results normally (d) and formatted to two decimal places (e)
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division: {:.2f}".format(a / b))
print("Integer Division:", a // b)
print("Modulus (Remainder):", a % b)
print("Exponentiation (Power):", a ** b)

import math

radius_str = input("Enter the radius of the circle: ")
radius = float(radius_str)

# Calculate Area (A = pi * r^2) and Circumference (C = 2 * pi * r)
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius

print("Area of the circle: {:.2f}".format(area))
print("Circumference of the circle: {:.2f}".format(circumference))

# Question 2
# (a) & (b) Accept space-separated numbers with robust validation loops
while True:
    user_input = input("Enter two numbers separated by a space: ")
    parts = user_input.split()
    
    # Verify exactly two items were entered
    if len(parts) != 2:
        print("Error: Please enter exactly two values.")
        continue
        
    try:
        num1 = float(parts[0])
        num2 = float(parts[1])
        
        print("Addition:", num1 + num2)
        print("Subtraction:", num1 - num2)
        print("Multiplication:", num1 * num2)
        
        
        if num2 == 0:
            print("Division Error: Cannot divide by zero.")
        else:
            print("Division:", num1 / num2)
            
        break  
    except ValueError:
        print("Error: Invalid numerical input. Please try again.")

# (c) 
while True:
    try:
        valid_integer = int(input("Please enter an integer: "))
        print("Valid integer entered:", valid_integer)
        break
    except ValueError:
        print("Invalid choice! That was not a whole number.")


def read_number():
    while True:
        try:
            user_val = input("Enter a floating-point number: ")
            return float(user_val)
        except ValueError:
            print("Invalid input! Try entering a valid decimal number.")

import re

def parse_expression():
    expr = input("Enter an expression (e.g., 5.3+4.7): ").strip()
    
    
    pattern = r"^([-+]?\d*\.?\d+)\s*([+\-×÷*\/])\s*([-+]?\d*\.?\d+)$"
    match = re.match(pattern, expr)
    
    if not match:
        print("Invalid expression format.")
        return

    num1 = float(match.group(1))
    operator = match.group(2)
    num2 = float(match.group(3))
    
    if operator == "+":
        result = num1 + num2
    elif operator in ["-", "−"]:
        result = num1 - num2
    elif operator in ["*", "×"]:
        result = num1 * num2
    elif operator in ["/", "÷"]:
        if num2 == 0:
            print("Error: Division by zero.")
            return
        result = num1 / num2
        
    print("Result:", result)
    
# Question 3
while True:
    try:
        a = int(input("Enter first integer (a): "))
        b = int(input("Enter second integer (b): "))
        break
    except ValueError:
        print("Invalid entries. Numbers must be integers.")

if a > b:
    print("The larger number is a:", a)
elif b > a:
    print("The larger number is b:", b)
else:
    print("Both numbers are equal.")

try:
    temp = float(input("Enter temperature in Celsius: "))
    if temp < 20:
        print("Status: LOW")
    elif 20 <= temp <= 30:
        print("Status: NORMAL")
    else:
        print("Status: HIGH")
except ValueError:
    print("Please input a valid numeric value.")


# (c)
print("Even numbers:")
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")
print("\n")

# (d) 
print("Countdown:")
count = 10
while count >= 1:
    print(count, end=" ")
    count = count - 1
print("\n")

# (e) 
L = [3, 5, 7, 9, 11]
total_sum = 0
for element in L:
    total_sum = total_sum + element
print("Manual list sum:", total_sum)

# (f) 
n = int(input("Enter a positive integer n: "))
series_sum = 0
for i in range(1, n + 1):
    series_sum = series_sum + i
print("Sum of 1 to", n, "is:", series_sum)

readings = []
print("Enter temperatures (Type -1 to stop):")

while True:
    try:
        val = float(input("Reading: "))
        if val == -1:
            break
        readings.append(val)
    except ValueError:
        print("Invalid entry. Skipping.")

if len(readings) == 0:
    print("No valid readings were entered.")
else:
    total = 0
    highest = readings[0]
    lowest = readings[0]
    
    for r in readings:
        total += r
        if r > highest:
            highest = r
        if r < lowest:
            lowest = r
            
    avg = total / len(readings)
    print("Number of valid readings:", len(readings))
    print("Average temperature:", avg)
    print("Highest temperature:", highest)
    print("Lowest temperature:", lowest)


# Question 4
# (a) 
def square(x):
    return x * x

# (b) 
def calculate_area(length, width):
    return length * width

# (c) 
def analyze_list(numbers):
    if not numbers:
        return None, None, None
    
    total = 0
    highest = numbers[0]
    lowest = numbers[0]
    
    for num in numbers:
        total += num
        if num > highest:
            highest = num
        if num < lowest:
            lowest = num
            
    avg = total / len(numbers)
    return highest, lowest, avg

# (d) 
student = {
    "Name": "Godfred Bio",
    "Age": 21,
    "Programme": "Computer Science"
}
student["GPA"] = 10.0
print("Student Dictionary:", student)

# (e) 
students_list = [
    {"name": "Ama", "reg_no": "CSC211", "score": 85},
    {"name": "Kiriku", "reg_no": "CSC211", "score": 92},
    {"name": "Rabbi", "reg_no": "CSC211", "score": 78},
    {"name": "Pope", "reg_no": "CSC211", "score": 64},
    {"name": "Adwoa", "reg_no": "CSC211", "score": 89}
]
print("\nStudent Performance List:")
for s in students_list:
    print("Name:", s["name"], "| Score:", s["score"])

# (f) & (g) C
def classify_temperature(temp):
    if temp < 20:
        return "LOW"
    elif 20 <= temp <= 30:
        return "NORMAL"
    else:
        return "HIGH"

temperatures = [15.5, 22.0, 35.6, 18.0, 28.5]
print("\nBatch Classifications:")
for t in temperatures:
    print("Temp:", t, "-> Status:", classify_temperature(t))

# (h) 
def count_status(readings_list):
    counts = {"LOW": 0, "NORMAL": 0, "HIGH": 0}
    for r in readings_list:
        status = classify_temperature(r)
        counts[status] += 1
    return counts


# Question 5
import math

# (a) 

def calculate_sine(degrees):
    radians = math.radians(degrees)
    return math.sin(radians)

# (b)
def fibonacci_series(n):
    if n < 0: return []
    if n == 0: return [0]
    
    series = [0, 1]
    while len(series) <= n:
        next_term = series[-1] + series[-2]
        series.append(next_term)
    return series

# (c) 
def fibonacci_below_max(max_value):
    if max_value <= 0: return []
    series = [0, 1]
    while True:
        next_term = series[-1] + series[-2]
        if next_term >= max_value:
            break
        series.append(next_term)
    return series

# (d) 
def find_primes(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for check in range(2, int(num ** 0.5) + 1):
            if num % check == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# (e) 
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# (f) 
def geometric_series_sum(a, r, n):
    total = 0
    for k in range(n):
        total += a * (r ** k)
    return total

# (g) 
def harmonic_number(n):
    total = 0.0
    for k in range(1, n + 1):
        total += 1 / k
    return total

# (h) 
print("Fibonacci first 10 terms:", fibonacci_series(9))
print("Geometric first 10 terms:", [1 * (2**k) for k in range(10)])
print("Harmonic first 10 terms:", [round(harmonic_number(k), 2) for k in range(1, 11)])


# Question 6
import math

class MathSeries:
    def __init__(self):
        pass

    def fibonacci(self, n):
        if n < 0:
            raise ValueError("Fibonacci index cannot be negative.")
        if n == 0: return [0]
        series = [0, 1]
        while len(series) <= n:
            series.append(series[-1] + series[-2])
        return series

    def fibonacci_max(self, max_value):
        if max_value < 0:
            raise ValueError("Max threshold limit value cannot be negative.")
        series = [0, 1]
        while True:
            next_term = series[-1] + series[-2]
            if next_term >= max_value:
                break
            series.append(next_term)
        return series

    def primes(self, max_value):
        if max_value < 0:
            raise ValueError("Prime range boundary bound limit cannot be negative.")
        primes_list = []
        for num in range(2, max_value + 1):
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes_list.append(num)
        return primes_list

    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial argument numbers cannot be negative values.")
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res

    def geometric(self, a, r, n):
        if n <= 0:
            raise ValueError("Number of series array elements must be positive.")
        total = 0
        for k in range(n):
            total += a * (r ** k)
        return total

    def harmonic(self, n):
        if n <= 0:
            raise ValueError("Number of terms calculated elements must be greater than zero.")
        total = 0.0
        for k in range(1, n + 1):
            total += 1 / k
        return total
    

# Question 7
import random

# (a) 
class Device:
    def __init__(self, device_id, name):
        self.device_id = device_id
        self.name = name
        self.status = "offline"  

    def toggle(self):
        if self.status == "online":
            self.status = "offline"
        else:
            self.status = "online"

    def info(self):
        return "ID: " + str(self.device_id) + " | Name: " + self.name + " | Status: " + self.status


# (b) 
class TemperatureSensor(Device):
    def __init__(self, device_id, name):
        super().__init__(device_id, name)
        self.temperature = 0.0

    def read(self):
        
        self.temperature = round(random.uniform(15.0, 40.0), 1)
        return self.temperature


# (c) 
class MotionSensor(Device):
    def __init__(self, device_id, name):
        super().__init__(device_id, name)
        self.motion_detected = False

    def read(self):
        # Randomly toggle flag indicator states
        self.motion_detected = random.choice([True, False])
        return self.motion_detected


# (d), (e), & (f) 
sensors = [
    TemperatureSensor(101, "Kitchen Temp"),
    TemperatureSensor(102, "Bedroom Temp"),
    TemperatureSensor(103, "Living Room Temp"),
    MotionSensor(201, "Front Door Motion"),
    MotionSensor(202, "Backyard Motion")
]

print("--- Initial Smart Home Device Network Status Logs ---")
for s in sensors:
    # online
    s.toggle()
    print(s.info())

print("\n--- Gathering Real-Time Environmental Sensor Reading Parameters ---")
for s in sensors:
    if isinstance(s, TemperatureSensor):
        print(s.name, "reports Temperature level at:", s.read(), "°C")
    elif isinstance(s, MotionSensor):
        print(s.name, "reports Active Motion detected state status:", s.read())


