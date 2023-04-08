#Addison Olstad
#CSCI 102 - Section C
#Assessment 09
#References: Zybooks chapter on random seeds and reading in files
#Time: 50 minutes

import random

'''Problem Statement'''
#Write a program that has the user input an integer
#Which rep a length of a word the user desires
#Your code should then output to the console:
#     1. the number of words int he dictionary that have the same length
#     2. a random word of that length

'''Specifically'''
#Read in the dictionary file
#prompt the user to enter the word length
#Prompt the user to enter a seed for random
#output the number of words in the dictionary that have length N
#Seed the random function with seed
#Of the words that have length N, choose one word randomly and output it

#input print statements
print("Enter the seed to use:")
seed_input = input("SEED> ")
print("Enter the length of words to find:")
length = int(input("LENGTH> "))

#reading in file
f = open("dictionary.txt")
words = f.readlines()
f.close()

#looping through file, counting number of words with correct length and adding them to a list
count_words = 0
words_of_length = []
for word in words:
    word = word.strip()
    if len(word) == length:
        count_words += 1
        words_of_length.append(word)

#output print statements, and seeding from list
if count_words > 1:
    random.seed(seed_input)
    ran_num = random.randint(0, len(words_of_length))
    print(f'Here is a random word with length {length}:')
    print("OUTPUT", end=" ")
    print(words_of_length[ran_num])
    print(f'The number of words with length {length} is:')
    print(f'OUTPUT {count_words}')
elif count_words == 1:
    print(f'Here is the only word with length {length}:')
    print("OUTPUT", end=" ")
    print(words_of_length[0])
    print(f'The number of words with length {length} is:')
    print("OUTPUT 1")
else:
    print(f'There are no words of length {length} in the dictionary.')
    print(f'OUTPUT None')
    print(f'The number of words with length {length} is:')
    print("OUTPUT 0")

