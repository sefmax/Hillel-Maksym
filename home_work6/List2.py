my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

divided = len(my_list) // 2
list1 = my_list[:divided]
list2 = my_list[divided:]

if len(list1) == len(list2):
    new_list = [list1, list2]
    print(new_list)

elif len(list1) != len(list2):
    x = list2.pop(0)
    list1.insert(-1, x)
    new_list = [sorted(list1), sorted(list2)]
    print(new_list)

elif len(list1) >= 1 and len(list2) == 0:
    x = list1[:divided]
    y = [x, list2]
    new_list = [list1, list2]
    print(new_list)

else:
    new_list = [list1, list2]
    print(new_list)
