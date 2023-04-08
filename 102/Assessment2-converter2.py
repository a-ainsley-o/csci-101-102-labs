#Addison Olsatd
#CSCI 101 - Section H
#Python Assessment 2
#References: My friend alex helped me with how to format the conversions
#Time: Like ten years

#Prompting conversion types
print("Choose one of the following converstions:")
print("1 - Binary-Decimal Conversion\n2 - Decimal-Binary Conversion")

conv_type = int(input("OPTION> "))
bd_num = input("Value> ")
length_1 = int(len(bd_num)) - 1
length = int(len(bd_num))
index = 0
count = 0
b_list = ''
d_list = ''

def binary_checker(string):
    '''Checks if string is binary'''
    for i in string:
        if i not in "10":
            return "False"
    return "True"

def decimal_checker(string):
    '''Checks if string is a decimal'''
    for i in string:
        if i not in "1234567890":
            return "False"
    return "True"    
if i in bd_num in "10" or bd_num in "1234567890":
    while conv_type == 1:
        if bd_num[index] == '1':
            count = count + 2 ** 1
            length_1 -= 1
            index += 1
            if index == length:
                print(f'OUTPUT {count}')
                break
        else:
            length_1 -= 1
            index += 1
            if index == length:
                print(f'OUTPUT {count}')
                break

    while conv_type == 2:
        if int(bd_num) >= 1:
            index = int(bd_num) % 2
            if index == 1:
                b_list += "1"
            else:
                b_list += "0"
            bd_num = int(bd_num) // 2
        if int(bd_num) < 1:
            i = len(b_list) - 1
            for i in range(i, -1, -1):
                d_list += b_list[i]
            print(f'OUTPUT {d_list}')
            break
else:
    print("OUTPUT Not a binary/decimal number")
        
