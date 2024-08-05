# tuples = an ordered list which is unchangeable. Used to group related data together

student = ("Om", 15, "male")
print(student)
print(student.count("Om"))
print(student.index("Om"))

for i in student:
    print(i)
if "Om" in student:
    print("Om is here!")
