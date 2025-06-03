x = [1, 2, 3, 4, 5]

if len(x) > 0:
    value = x.pop(-1)
    x.insert(0, value)
    print(x)

else:
    print(x)