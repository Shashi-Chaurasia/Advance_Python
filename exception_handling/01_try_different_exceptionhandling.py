try:
    a = int(input("Enter Number : "))
    c = 1/a
    print(c)

except ZeroDivisionError as e:
    print("make sure you input is not zero")

except TypeError as e:
    print("Type error")

except Exception as e:
    print("plz chake your input type")