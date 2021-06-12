# try:
#     a = int(input("Eneter Number : "))
#     c = 1/a

# except:
#     raise ValueError("this input are not integer : ")


def increase(num):
    try:
        return int(num) + 1

    except:
        raise ValueError("this is not good input")

a = increase(5)
print(a)

b = increase('jkdfjh9859fnk48394830')
print(b)


c = increase(90)
print(c)
