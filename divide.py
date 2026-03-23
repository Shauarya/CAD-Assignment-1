def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = divide(num1, num2)

print("Division is:", result)