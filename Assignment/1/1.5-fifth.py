"""Check if a number is a mirror number."""
given_number = int(input())
original_number = given_number
reverse = 0

while given_number > 0:
    reminder = given_number % 10
    reverse = reverse * 10 + reminder
    given_number = given_number // 10

if original_number == reverse:
    print("Mirror Number")
else:
    print("Not Mirror Number")
