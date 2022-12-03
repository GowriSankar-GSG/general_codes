# Program to find the ASCII value of the given character

c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))

# Program to find the ASCII value of the given string

print("Enter a String: ", end="")
text = input()
textlength = len(text)
for char in text:
    ascii = ord(char)
    print(char, "\t", ascii)
