# Strings can be created by enclosing a character or group of characters inside single (' ') or double (" ") quotes.
# Even triple quotes can be used in Python but generally used to represent multiline strings and docstrings.

# Single quotes
myString1 = 'Hello'
myString2 = "Hello"
myString3 = '''Hello'''
print(myString1, myString2, myString3)
 

myString = "Hello"
 
print(myString[0]) # Print the first character
print(myString[-1]) # Print the last character using negative indexing
print(myString[2:5]) # Slicing 2nd to 5th character

# If we try to access indexes out of the range or use decimal numbers, we will get errors.
# print(myString[18])
# print(myString[1.6])

myString= "Hello"
# myString[4] = 'S' #strings are immutable
del myString # delete complete string
#print(myString)

# String supports concatenation and repetition.
c="a" + "b"
d="ha" * 4
print(c,d)

# Initializing count to 0
count = 0
# Iterating through each character in the string "Hello World"
for char in "Hello World":
    if char == 'l':  # Checking if the character is 'l'
        count += 1
print(f"{count} letters found")

print('l' in 'Hello World') #in operator to test membership
print('or' in 'Hello World')

# Methods in String

my_string = "   Hello, World!   "

length = len(my_string) # 1. len()
lower_case = my_string.lower() # 2. lower() and upper()
upper_case = my_string.upper() 
stripped = my_string.strip() # 3. strip(), lstrip(), and rstrip()
left_stripped = my_string.lstrip()
right_stripped = my_string.rstrip()
index1 = my_string.find("World") # 4. find() and index()
index2 = my_string.index("World")
new_string = my_string.replace("World", "Universe") # 5. replace()
parts = my_string.split(", ") # 6. split()
joined_string = ', '.join(parts) # 7. join()
starts_with = my_string.startswith("Hello") # 8. startswith() and endswith()
ends_with = my_string.endswith("World!")
print("Length:", length) # Displaying results
print("Lowercase:", lower_case)
print("Uppercase:", upper_case)
print("Stripped:", stripped)
print("Left Stripped:", left_stripped)
print("Right Stripped:", right_stripped)
print("Index (find()):", index1)
print("Index (index()):", index2)
print("Replaced:", new_string)
print("Split:", parts)
print("Joined:", joined_string)
print("Starts with 'Hello':", starts_with)
print("Ends with 'World!':", ends_with)