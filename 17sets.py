# set = collection which is unordered and unindexed . Auto removes the duplicate values.

utensils = {"spoon", "fork", "plate"}
not_utensils = {"key", "board", "switch"}
print(utensils)
utensils.add("cup")
print(utensils)
utensils.remove("plate")
print(utensils)
utensils.clear()
print(utensils)
utensils.update(not_utensils)
print(utensils)
var = utensils.union(not_utensils)
for i in var:
    print(i)
print(utensils.difference(not_utensils))
print(utensils.intersection(not_utensils))

