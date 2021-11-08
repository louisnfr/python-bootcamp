import sys

def error():
	print("ERROR")
	exit()

if (len(sys.argv) > 2):
	error()
	
try:
	num = int(sys.argv[1])
except:
	error()

if (num % 2) == 0:
   print("I'm Even.")
else:
   print("I'm Odd.")
