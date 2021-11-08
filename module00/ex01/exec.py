import sys

argv = sys.argv[1:]
string = ' '.join(argv)
rev_string = string[::-1]
print(rev_string.swapcase())
