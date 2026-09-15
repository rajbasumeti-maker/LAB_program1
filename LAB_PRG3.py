num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"Before swapping: First number is {num1} and second number is {num2}")

temp = num1
num1 = num2
num2 = temp

print(f"After swapping: First number is {num1} and second number is {num2}")