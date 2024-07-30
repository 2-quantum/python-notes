# Order of the statement matters if the first condition is met it will not check for other and will exit the if else statement.

age = int(input("What is your age: "))

if age < 0:
    print("You are not born yet.")
elif age < 18:
    print("You are not adult.")
elif age > 100:
    print("You lived a long life.")
else:
    print("You are an adult.")
