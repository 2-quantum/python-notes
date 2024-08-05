# 2d list = a list of lists

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list3 = [11, 12, 13]

list_all = [list1, list2, list3]
print(list_all)  # print all
print(list_all[0])  # print the first list only
print(list_all[0][0])  # print the first thing of the first list
print(list_all[2][3])  # IndexError this index not in the list
