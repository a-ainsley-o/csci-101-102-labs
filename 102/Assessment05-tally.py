#Addison Olstad
#CSCI 102 - Section H
#Assessment 05A
#References: None
#Time: 25 minutes

#prompting statement
print("Enter values to add. Enter quit when done.")

#inputs
count = 0
sum_num = 0
while True:
    i = input("NUMBER> ")
    if i == "quit":
        break
    else:
        i = int(i)
        count += 1
        sum_num += i

#print statements
print(f'The addition of the {count} numbers entered is:')
print(f'OUTPUT {count} numbers')
print(f'OUTPUT {sum_num} total')
