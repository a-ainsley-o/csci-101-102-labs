#Addison Olstad
#CSCI 101 - Section C
#Python Lab 5
#References: TA Thor helped me sort of the initial functions
#Time: 5 days

def telsatower(x, y):
    '''Powers buildings on, 1 block surrounding'''
    t1 = 0
    t2 = 0
    #print("Pre for loop")
    for i in range(-1,2,1):
        for j in range(-1,2,1):
            t1 = x + i
            t2 = y + j
            #print("telsatower is running pre if statement")
            if t1 >= 0 and t2 >= 0 and t1 < rows and t2 < columns:
                if array[t1][t2] == "b":
                    array[t1][t2] = "L"
                #print("telsatower is running")
            

def supertower(x, y):
    '''Powers buildings on, 2 blocks surrounding'''
    t1 = 0
    t2 = 0
    for i in range(-2, 3,1):
        for j in range(-2,3,1):
            t1 = x + i
            t2 = y + j
            if t1 >= 0 and t2 >= 0 and t1 < rows and t2 < columns:
                if array[t1][t2] == "b":
                    array[t1][t2] = "L"

#Intro print statements
print("Input the number of rows and columns in the subdivision:")
rows = int(input("ROWS> "))
columns = int(input("COLUMNS> "))

#Setting up row print statements
array = []
print("Input each row of the subdivison:")
for i in range(0, rows, 1):
    print(f'Row{i}>', end = " ")
    row = input()
    row_hehe = row.split(' ')
    array.append(row_hehe)

#looping through array, checking functions
#in rows
for i in range(rows):
    #in columns
    for j in range(columns):
        if array[i][j] == "T":
            telsatower(i, j)
        if array[i][j] == "S":
            supertower(i, j)

#Adding non powered buildings to a list
power_level = ""
not_lit = []
for i in range(rows):
    for j in range(columns):
        if array[i][j] == "b":
            coordinates = [i,j]
            power_level += "False"
            not_lit.append(coordinates)
            
#Determining whether output false or true based on if not_lit list has entries
if "False" in power_level:
    print("Not all buildings are powered!")
    print("OUTPUT False")
    print("The following buildings are not powered:")
    print(f'OUTPUT', end=" ")
    print(not_lit)
else:
    print("All buildings are powered!")
    print("OUTPUT True")


            
