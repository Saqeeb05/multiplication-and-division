num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))

mul = num1 * num2
# Check for division by zero
if num2 != 0:
    div = num1 / num2
    print(f"Multiplication of two numbers: {mul}")
    print(f"Division of two numbers: {div}")
else:
    print(f"Multiplication of two numbers: {mul}")
    print("Division by zero is not allowed.")