class Calculator:
    def __init__(self, a: float, b:float, operation: str):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both operands must be numeric (int or float).")
        if not isinstance(operation, str):
            raise TypeError("Operation must be a string.")

        self.a = a
        self.b = b
        self.operation = operation

    def calculate(self) -> float:
        if self.operation == "+":
            return self.a + self.b
        elif self.operation == "-":
            return self.a - self.b
        elif self.operation == "*":
            return self.a * self.b
        elif self.operation == "/":
            if self.b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return self.a / self.b
        else:
            raise Exception("Invalid operation")


