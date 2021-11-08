import sys

def punct_count(string):
	count = 0
	for i in range(0, len(string)):
		if string[i] in ('!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?"):
			count = count + 1;
	return count

def text_analyzer(*args):
	if (len(args) == 0):
		print("What is the text to analyse?")
		return
	elif (len(args) > 1):
		print("ERROR")
		return
	else:
		text = args[0];
	"This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."
	print("The text contains", len(text), "characters:")
	print("-", sum(1 for c in text if c.isupper()), "upper letters")
	print("-", sum(1 for c in text if c.islower()), "lower letters")
	print("-", punct_count(text), "punctuation marks")
	print("-", text.count(" "), "spaces")
