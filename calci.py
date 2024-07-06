# calculator.py

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    """Returns the division of a by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def calculate(expression):
    """
    Evaluates a basic arithmetic expression.
    
    Args:
    expression (str): The arithmetic expression to evaluate.

    Returns:
    float: The result of the arithmetic operation.

    Raises:
    ValueError: If the expression is invalid.
    """
    try:
        # Split the expression into components
        components = expression.split()
        
        if len(components) != 3:
            raise ValueError("Invalid format. Use: operand1 operator operand2")
        
        operand1, operator, operand2 = components
        operand1 = float(operand1)
        operand2 = float(operand2)
        
        if operator == '+':
            return add(operand1, operand2)
        elif operator == '-':
            return subtract(operand1, operand2)
        elif operator == '*':
            return multiply(operand1, operand2)
        elif operator == '/':
            return divide(operand1, operand2)
        else:
            raise ValueError("Unsupported operator. Use +, -, *, or /")
    except ValueError as e:
        raise ValueError(f"Error evaluating expression: {e}")

def main():
    """Main function to run the calculator."""
    print("Text-based Calculator")
    print("Enter expressions in the format: operand1 operator operand2 (e.g., 3 + 4)")
    print("Type 'quit' to exit the calculator.")
    
    while True:
        try:
            expression = input("Enter expression: ")
            if expression.lower() == 'quit':
                break
            result = calculate(expression)
            print(f"Result: {result}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
