#John Henke
#CSCI 101 - Section H
#Python Assessment 2
#References: My friend alex helped me with how to format the conversions
#Time: Like ten years

#Prompting conversion types
print("Choose one of the following converstions:")
print("1 - Binary-Decimal Conversion\n2 - Decimal-Binary Conversion")
conv_type = int(input("OPTION> "))

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

#Splitting between options
if conv_type == 1:

    #Prompting for a binary number
    binary_str = input("Binary-String> ")
    value = binary_checker(binary_str)
    if value == "False":
        print(f'{binary_str} is not a Binary Number.')
    else:
        while conv_type == 1:
            index = 0
            decimal_new = 0
            length_str = int(len(binary_str))
            str_length = int(len(binary_str)) - 1

            if binary_str[index] == '1':
                decimal_new = decimal_new + 2 ** 1
                str_length -= 1
                index += 1
                if index == length_str:
                    print(f'OUTPUT {decimal_new}')
                    break

            else:
                str_length -= 1
                index += 1
                if index == length_str:
                    print(f'OUTPUT {decimal_new}')
                    break

elif conv_type == 2:

    #prompting for a decimal number
    decimal_str = input("Decimal-String> ")
    value = decimal_checker(decimal_str)
    if value == "False":
        print(f'{decimal_str} is not a Decimal Number.')
    else:
        while conv_type == 2:
            index = 0
            binary_new = ''
            oth_binary = ''
            length_str = int(len(decimal_str))
            str_length = int(len(decimal_str)) - 1

            if int(decimal_str) >= 1:
                index = int(decimal_str) % 2
                if decimal_str == 1:
                    binary_new += '1'
                else:
                    binary_new += '0'
                decimal_str = int(decimal_str) // 2

            if int(decimal_str) < 1:
                str_length = len(binary_new) - 1
                for i in range(i, -1, -1):
                    oth_binary += binary_new[i]
                print(f'OUTPUT {oth_binary}')
                break
    
else:
    print(f'{conv_type} is not an option')
    
