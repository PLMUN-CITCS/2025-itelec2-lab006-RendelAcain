import math

# 1. Calculate the square root of a number (e.g., 16)
number = 16
sqrt_result = math.sqrt(number)

# 2. Access the value of pi (π)
pi_value = math.pi

# 3. Convert degrees to radians and calculate sine, cosine, and tangent
angle_degrees = 30
angle_radians = math.radians(angle_degrees)  # Important to convert degrees to radians first

# Calculating the sine, cosine, and tangent of the angle in radians
sin_result = math.sin(angle_radians)
cos_result = math.cos(angle_radians)
tan_result = math.tan(angle_radians)

# 4. Calculate the exponential of a number (e.g., 2)
exp_result = math.exp(2)

# 5. Calculate the natural logarithm (base e) of a number (e.g., 10)
log_result = math.log(10)

# 6. Calculate the logarithm (base 10) of a number (e.g., 100)
log10_result = math.log(100, 10)

# Display the results with descriptive labels
print("Square root of", number, "is:", sqrt_result)
print("Value of pi is:", pi_value)
print("Sine of", angle_degrees, "degrees (in radians) is:", sin_result)
print("Cosine of", 60, "degrees (in radians) is:", cos_result)
print("Tangent of", 45, "degrees (in radians) is:", tan_result)
print("Exponential of 2 is:", exp_result)
print("Logarithm (base e) of 10 is:", log_result)
print("Logarithm (base 10) of 100 is:", log10_result)
