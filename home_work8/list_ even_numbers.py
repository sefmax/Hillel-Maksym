#[0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88


LIST = [0, 1, 7, 2, 4, 8]

if len(LIST) == 0:
    print(0)
else:
    elements = [x for x in LIST if LIST.index(x) % 2 == 0]
    result = sum(elements,0) * LIST[-1]
    print(result)
