#Addison, Jaxson, Ben
#CSCI102 - Section H
#Peer Review Assessment 03

#prompting input for numbers
print("Welcome to our Enhanced Calculator!")
print("Input the first operand.")
operand_one = float(input("FIRST> "))
print("Input the second operand.")
operand_two = float(input("SECOND> "))

#prompting operation options
print("Choose one of the following operations:")
print('1 - addition\n2- subtraction\n3 - multiplication\n4 - divison')

#prompting input
operation = int(input("OPERATION> "))

#if else for different numbers
#addition then subtraction then multiplication, then division
if operation == 1:
    sum = operand_one + operand_two
    print(f'OUTPUT {sum:.6f}')
elif operation == 2:
    difference = operand_one - operand_two
    print(f'OUTPUT {difference:.6f}')
elif operation == 3:
    product = operand_one * operand_two
    print(f'OUTPUT {product:.6f}')
elif operation == 4:
    quotient = operand_one // operand_two
    remainder = operand_one % operand_two
    print("OUTPUT", int(round(quotient, 0)))
    print("OUTPUT", int(round(remainder, 0)))
else:
    print("We only except values of 1, 2, 3, 4")

print("Thank you for using our Enhanced Calculator!")











