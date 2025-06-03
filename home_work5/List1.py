x = [1, 2, 3, 4, 5]

if len(x) > 0:
    value = x.pop(-1)
    x.insert(0, value)
    print(x)

elif len(x) == 1:
    print(x)

#elif len(x) == 0:
 #   print(x)
 #   print('zero')
else:
    print(x)