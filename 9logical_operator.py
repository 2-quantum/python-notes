# logical operator (and, or, not)

temp = int(input("What is the temperature: "))

if temp < 0 or temp > 30:
    print("Temperature is not good")
elif temp > 0 and temp < 30:
    print("Temperature is good.")
else:
    print("Your temp is either 0 or 30")

age = int(input("Enter your age : "))

if not (age >= 0):
    print("You are not born")
elif not (age >= 18):
    print("You are not adult")
elif not (age <= 18):
    print("You are an adult.")
else:
    print("I dont think this will run.")
