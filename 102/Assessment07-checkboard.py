#Addison Olstad
#CSCI 102 - Section H
#Assessment 07
#References: None
#Time: 30 minutes

#a checker board generator

print("How many columns does the checkerboard have?")
col = int(input("COLUMN> "))

print("How many rows does the checkboard have?")
row = int(input("ROWS> "))

print("What are the strings with which to pattern it?")
first = input("FIRST> ")
second = input("SECOND> ")

print(f'A checkerboard with {row} rows, {col} columns, first string is {first}, and second string is {second} is:')

#making even list
even = []
for i in range(0, 100, 2):
    even.append(i)

#making odd list
odd = []
for i in range(1, 100, 2):
    odd.append(i)

count = 0
array = []

#while count is less than the row number
while count < row:
    check_row = []

    #for i range of the range of columns
    for i in range(0, col, 1):
        if i == 0:

            #alternating between appending
            if count in even:
                check_row.append(first)
            else:
                check_row.append(second)
        elif check_row[i-1] == first:
            check_row.append(second)
        elif check_row[i-1] == second:
            check_row.append(first)
    array.append(check_row)
    print("OUTPUT", end=" ")
    print(check_row)
    count += 1

print("And the 2D array representation is:")
print("OUTPUT", end=" ")
print(array)

            
    
    
