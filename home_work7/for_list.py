
z = [100, 0, 200, 0, 50, 0, 1, 2, 3, 0]

x = [x for x in z if x != 0]
y =[0] * z.count(0)
print(x + y)
