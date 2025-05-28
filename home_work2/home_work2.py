numb = input("Please enter a 5 digit number: ")

numb = int(numb)

numb1 = numb % 10
numb2 = numb // 10 % 10
numb3 = numb // 100 % 10
numb4 = numb // 1000 % 10
numb5 = numb // 10000 % 10
reverse_numb = numb1 * 10000 + numb2 * 1000 + numb3 * 100 + numb4 * 10 + numb5 * 1

print(reverse_numb)