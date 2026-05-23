# string methods
# capitalize() - Converts the first character to upper case
# casefold() - Converts string into lower case
# center() - Returns a centered string
# count() - Returns the number of times a specified value occurs in a string
# encode() - Returns an encoded version of the string
# endswith() - Returns true if the string ends with the specified value
# expandtabs() - Sets the tab size of the string
# find() - Searches the string for a specified value and returns the position of where it was found
# format() - Formats specified values in a string
# format_map() - Formats specified values in a string
# index() - Searches the string for a specified value and returns the position of where it was found
# isalnum() - Returns True if all characters in the string are alphanumeric
# isalpha() - Returns True if all characters in the string are in the alphabet
# isdecimal() - Returns True if all characters in the string are decimals
# isdigit() - Returns True if all characters in the string are digits
# isidentifier() - Returns True if the string is an identifier
# islower() - Returns True if all characters in the string are lower case
# isnumeric() - Returns True if all characters in the string are numeric
# isprintable() - Returns True if all characters in the string are printable
# isspace() - Returns True if all characters in the string are whitespaces
# istitle() - Returns True if the string follows the rules of a title
# isupper() - Returns True if all characters in the string are upper case
# join() - Joins the elements of an iterable to the end of the string
# lstrip() - Returns a left trim version of the string
# maketrans() - Returns a translation table to be used in translations
# partition() - Returns a tuple where the string is parted into three parts
# replace() - Returns a string where a specified value is replaced with a specified value
# rfind() - Searches the string for a specified value and returns the last position of where it was found
# rindex() - Searches the string for a specified value and returns the last position of where
# it was found
# rjust() - Returns a right justified version of the string
# rpartition() - Returns a tuple where the string is parted into three parts
# rsplit() - Splits the string at the specified separator, and returns a list
# rstrip() - Returns a right trim version of the string
# split() - Splits the string at the specified separator, and returns a list
# splitlines() - Splits the string at line breaks and returns a list
# startswith() - Returns true if the string starts with the specified value
# strip() - Returns a trimmed version of the string
# swapcase() - Swaps cases, lower case becomes upper case and vice versa
# title() - Converts the first character of each word to upper case
# translate() - Returns a translated string
# upper() - Converts a string into upper case
# zfill() - Fills the string with a specified number of 0 values at the
# beginning of the string

message = "hello World, welcome to Bangladesh. "
print(message.capitalize()) # Output: Hello world, welcome to bangladesh. 
print(message.casefold()) # Output: hello world, welcome to bangladesh. 
print(message.center(50)) # Output:     hello world, welcome to bangladesh.
print(message.count("a")) # Output: 2
print(message.endswith("world.")) # Output: False
print(message.expandtabs(4)) # Output: hello World, welcome to Bangladesh.
print(message.find("beautiful")) # Output: -1
print(message.format()) # Output: hello World, welcome to Bangladesh.
print(message.index("welcome")) # Output: 13
print(message.isalnum()) # Output: False
print(message.isalpha()) # Output: False
print(message.isdecimal()) # Output: False
print(message.isdigit()) # Output: False
print(message.isidentifier()) # Output: False
print(message.islower()) # Output: False
print(message.isnumeric()) # Output: False
print(message.isprintable()) # Output: True
print(message.isspace()) # Output: False
print(message.istitle()) # Output: False
print(message.isupper()) # Output: False
print(message.join("Hello")) # Output:  Hhello World, welcome to Bangladesh. ehello World, welcome to Bangladesh. lhello World, welcome to Bangladesh. lhello World, welcome to Bangladesh. ohello World, welcome to Bangladesh.
print(message.lstrip()) # Output: Bangladesh is a beautiful country in the world.
print(message.partition("beautiful")) # Output: ('Bangladesh is a ', 'beautiful', ' country in the world.')
print(message.replace("beautiful", "wonderful")) # Output: Bangladesh is a wonderful country in the world.
print(message.rjust(50)) # Output:     Bangladesh is a beautiful country in the world.
print(message.rpartition("beautiful")) # Output: ('Bangladesh is a ', 'beautiful', ' country in the world.')
print(message.rsplit()) # Output: ['Bangladesh', 'is', 'a', 'beautiful', 'country', 'in', 'the', 'world.']
print(message.rfind("a")) # Output: 38
print(message.rindex("a")) # Output: 38
print(message.rstrip()) # Output: Bangladesh is a beautiful country in the world.
print(message.split()) # Output: ['Bangladesh', 'is', 'a', 'beautiful', 'country', 'in', 'the', 'world.']
print(message.splitlines()) # Output: ['Bangladesh is a beautiful country in the world.']
print(message.startswith("Bangladesh")) # Output: True
print(message.strip()) # Output: Bangladesh is a beautiful country in the world.
print(message.swapcase()) # Output: bANGLADESH IS A BEAUTIFUL COUNTRY IN THE WORLD.
print(message.title()) # Output: Bangladesh Is A Beautiful Country In The World.
print(message.translate(str.maketrans("a", "A"))) # Output: BAngladesh is A beAutiful country in the world.
print(message.upper()) # Output: BANGLADESH IS A BEAUTIFUL COUNTRY IN THE WORLD.
print(message.zfill(50)) # Output: 000000000000000Bangladesh is a beautiful country in the world.

