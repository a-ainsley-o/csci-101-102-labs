#Addison Olstad
#CSCI 102 - Section H
#Assessment 08A
#References: The python guide for the random/randrange function on pynative.
#Time: 20 minutes

#importing libraries
import random

#print input function
print("Input the seed for the random number generator: ")
seed = int(input("SEED> "))

print("Input the number of rolls to make:")
rolls = int(input("ROLLS> "))

print("Input the number of sides of the die:")
sides = int(input("SIDES> "))

#defining how to keep track of the rolls
rolls_fin = [0] * sides

#seeding the random
random.seed(seed)

#iterating through each roll

for i in range(rolls):
    
    #randomly choosing which side was rolled and adding to rolls_fin
    rolls_fin[random.randrange(0,sides)] += 1

#final print statement
print(f'Your {rolls} rolls of a {sides}-sided die follow:')

x = 1
#while the counter is under the amount of sides
while x <= sides:
    
    #will print out this print statement [x] amount of times until x>sides
    print(f'OUTPUT {x} occurred {rolls_fin[x-1]} times')

    #adding to counter
    x += 1
