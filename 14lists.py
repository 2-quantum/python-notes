# list = used to store multiple items in a single variable

sports = ["cricket", "hockey", "chess"]
print(sports)  # print all the thing in sport as list
print(sports[0])  # print the sport at index 1
for i in sports:
    print(i)  # print every sports one by one
sports.append("appended")
print(sports)
sports.remove("appended")
print(sports)
sports.pop()
print(sports)
sports.reverse()
print(sports)
sports.insert(0, "inserted")
print(sports)
sports.sort()
print(sports)
sports.clear()
print(sports)
