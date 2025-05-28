numb = input("Please enter a 5 digit number: ")

numb = int(numb)

numb1 = numb % 10
numb2 = numb // 10 % 10
numb3 = numb // 100 % 10
numb4 = numb // 1000 % 10
numb5 = numb // 10000 % 10

print(numb1, numb2, numb3, numb4, numb5)