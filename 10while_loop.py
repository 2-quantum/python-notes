# while loop continues until the condition in it doesn't meet.

name = ""

while len(name) == 0:
    name = input("What is your name: ")

age = None

while not age:
    age = input("What is your age: ")
    if age:
        age = int(age)
print(f"Your name is {name} and age is {age}")

