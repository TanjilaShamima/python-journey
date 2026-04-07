fruits = ["Apple", "Banana", "Cherry", "Orange", "Kiwi", "Melon", "Mango"]

for x in fruits:
    print(x)

print([x for x in fruits])

for x in fruits:
    if "a" in x:
        print(x, end=", ")

print("")

newList = [x for x in fruits if "a" in x]
print(newList)