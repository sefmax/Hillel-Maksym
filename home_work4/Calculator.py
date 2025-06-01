numb1 = int(input("Enter first number: "))
operation = input ("Select operation: ")
numb2 = int(input("Enter second number: "))


if operation == "/" and numb2 != 0:
    print(numb1 / numb2)
elif operation == "*":
    print(numb1 * numb2)
elif operation == "+":
    print(numb1 + numb2)
elif operation == "-":
    print(numb1 - numb2)
else:
    print("unknown operation")




