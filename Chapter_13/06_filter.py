def greater_than_5(num):
    if num > 5:
        return True
    else:
        return False

l1 = [2468,243,1,2,453,1,3,4,5,1,34,954,5,56,24,3,45,2,45,1]
print(list(filter(greater_than_5, l1)))