def divisible_by_5(list1):
    if list1 % 5== 0:
        return True
    else:
        return False

list1 = [5,56,4,676,2335,676,343,40,100,150,245,354,345]
print(list(filter(divisible_by_5 , list1)))

