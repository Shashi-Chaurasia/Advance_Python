from functools import reduce
list1 = [2, 5324, 2, 55, 2425, 64, 356, 68, 435, 87, 3568, 468, 9, 46, 24]
a = reduce(max, list1)
print(a)
 