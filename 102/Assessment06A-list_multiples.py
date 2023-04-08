#Addison Olstad
#CSCI 102 - Section H
#Assessment 06A
#References: None
#Time: 10 minutes

#Reads two numers, num and max_index
#for loop to create a list of multiples
#of num until list length reaches max_index + 1


#input print statements
print("Enter the number to create multiples for.")
num = int(input("NUMBER> "))
print("Enter the maximun index of the list.")
max_input = int(input("INDEX> "))

#empty count
count = 0
#Empty list
multi_list = []

#for i in range of the index range
for i in range(0, max_input + 1, 1):
    #list appens with each multiple
    multi_list.append(num + (num*i))

#print OUTPUT statements
print("Your list of multiples is as follows:")
print("OUTPUT", end=" ")
print(multi_list)

first_multi = multi_list[0]

print("The first multiple calculated is:")
print(f'OUTPUT {first_multi}')
