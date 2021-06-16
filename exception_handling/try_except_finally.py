
try:
    c = int(input('enter the number :'))
    d = 1/c
    print(d)

except ValueError as e:
    print("wrong input")

finally:
    print("done")