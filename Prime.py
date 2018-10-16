n = 20
x = 3
l = [2]
count = 0
while n > count:
    flag = 1
    for y in range(2, x):
        if x % y == 0:
            flag = 0
            break
    if flag == 1:
        l.append(x)
        count += 1
    x = x + 1
print(l)
