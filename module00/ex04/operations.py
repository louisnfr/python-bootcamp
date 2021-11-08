import sys

def error(msg):
	print(msg)
	exit()

if (len(sys.argv) <= 2):
	error("Usage: python operations.py <number1> <number2>")
if (len(sys.argv) > 3):
	error("inputError: too many arguments")

try:
	a = int(sys.argv[1])
	b = int(sys.argv[2])
except:
	error("inputError: only numbers")

print("Sum:\t\t", a + b)
print("Difference:\t", a - b)
print("Product:\t", a * b)
print("Quotient:\t", a / b) if b != 0 else print("Quotient:\tERROR (div by zero)")
print("Remainder:\t", a % b) if b != 0 else print("Remainder:\tERROR (modulo by zero)")
