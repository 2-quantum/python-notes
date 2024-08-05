# break - terminate the loop entirely
# continue - skips the next iteration of the loop
# pass - does nothing acts as placeholder i.e. where some code is necessary but we dont want to write it now or no code to execute here

while True:
    print("This is not infinite loop.")
    break
print("Name without space: ", end="")
for i in "Om Prabhat":
    if i == " ":
        continue
    print(i, end="")
for i in "Om Prabhat":
    pass  # this does nothing as this for loop takes atleast 1 arguent . So to avoid writing any unnecessary code just write pass
