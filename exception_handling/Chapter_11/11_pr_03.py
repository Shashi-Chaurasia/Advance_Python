# num = int(input("table of Number : "))

# table = [num * i for i in range(1,11)]
# print(table)

def mulTable(num):
    table = [num * i for i in range(1,11)]
    print(table)
    with open('table.txt', 'a') as f:
        f.write(str(table))
        f.write('\n')


num = int(input("Table of numbers : "))
mulTable(num)


