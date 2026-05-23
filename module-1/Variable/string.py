b = "Hello World"

print(b[2:7]) # Output: llo W
print(b[:8]) # Output: Hello Wo
print(b[3:8]) # Output: lo Wo
print(b[-7:-3]) # Output: llo W


a = "Bangladesh is a beautiful country in the world. "

print(a.upper()) # Output: BANGLADESH IS A BEAUTIFUL COUNTRY IN THE WORLD.
print(a.lower()) # Output: bangladesh is a beautiful country in the world.
print(a.strip()) # Output: Bangladesh is a beautiful country in the world.
print(a.replace("beautiful", "wonderful")) # Output: Bangladesh is a wonderful country in the world.
print(a.split()) # Output: ['Bangladesh', 'is', 'a', 'beautiful', 'country', 'in', 'the', 'world.']

price = 50

txt = f"The price is {price:.2f} dollars"
print(txt) # Output: The price is 50.00 dollars

text = "Python is a great \"programming\" language."
print(text) # Output: Python is a great "programming" language.

