def squares(num):
    return num * num

#Method -- 1  
l1 = [1,2,3,4]
l2 = []
for i in l1:
    l2.append(squares(i))

print(l2)

#Method ---2

print(list(map(squares , l1)))
