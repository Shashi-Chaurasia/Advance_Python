list1 = [2,4,2,6,9,346,7,5,34,6787,355,78789,34,76,34,8,43,79,43,89,3,798,
3,879,4,898,3,56,24,667,3,8,3,87,35,77,787,44,7,4]

# list2 = []

# for item in list1:
#     if ( item % 2 == 1):
#         list2.append(item)


# print(list2) 

list2 = [i for i in list1 if i >= 42]

print(list2)


