import math

# square root of a number
num = float(input("Enter a number to find its square root: "))
sqrt_value = math.sqrt(num)
print("Square root of", num, "is:", sqrt_value)

# sine of an angle (in degrees)
angle_deg = float(input("Enter an angle in degrees: "))
angle_rad = math.radians(angle_deg)   # convert degrees to radians
sine_value = math.sin(angle_rad)
print("Sine of", angle_deg, "degrees is:", sine_value)

# GCD of two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
gcd_value = math.gcd(num1, num2)
print("GCD of", num1, "and", num2, "is:", gcd_value)
