# TUGAS PEMOGRAMAN PYTHON
# by b01l3d3gg137

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

if __name__ == "__main__":
    print("Simple Calculator")
    print("Addition: 2 + 3 =", add(2, 3))
    print("Subtraction: 5 - 2 =", subtract(5, 2))
    print("Multiplication: 4 * 3 =", multiply(4, 3))
    print("Division: 10 / 2 =", divide(10, 2))
