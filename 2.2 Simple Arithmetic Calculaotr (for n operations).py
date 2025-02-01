#this code can perform simple Arithmetic operation on to integers,that are user input '
print("Give an Expression to : Ex 1*1")
while True:
    user_input= input("Enter the expression")
    if user_input == 'q':
        break
    else:
        operands = user_input.split()
        if len(operands) != 3:
            print("enter a valid statement ")
        else:
            num1 = float(operands[0])
            operator = operands[1]
            num2 = float(operands[2])

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator =='*':
                result = num1 * num2
            elif operator == '/':
                result = num1/num2
            else:
                print("invalid operator")

            print(f"result: {result}")