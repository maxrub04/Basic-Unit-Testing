from Calculator import Calculator

#cal=Calculator(a, b, operation)
calc = Calculator(1, 2, "+")
result = calc.calculate()
print("Result:", result)

calc = Calculator(2, 2, "-")
result = calc.calculate()
print("Result:", result)

calc = Calculator(3, 4, "*")
result = calc.calculate()
print("Result:", result)

calc = Calculator(1, 0, "/")
result = calc.calculate()
print("Result:", result)

calc = Calculator(1, 0, "I")
result = calc.calculate()
print("Result:", result)

