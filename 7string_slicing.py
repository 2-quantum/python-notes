# using indexing[] or slice() format indexing[start:stop:step] slice(start,stop,step)
# start is inclusive but stop is exclusive
# in indexing to specify the first and last we can also leave it blank
# when counting from left it starts from 0 and when counting from right it starts from -1

name = "Bat Quantum"

web1 = "https://google.com"
web2 = "https://wikipedia.com"

firstname = name[:3]
print(firstname)
lastname = name[4:]
print(lastname)
reversed_name = name[::-1]
print(reversed_name)

onlyname = slice(8, -4)
web1 = web1[onlyname]
web2 = web2[onlyname]
print(web1)
print(web2)
