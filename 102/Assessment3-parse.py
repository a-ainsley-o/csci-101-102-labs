#Addison Olstad
#CSCI 101 - Section H
#Python Assessment 3
#References: 
#Time:

import string

'''Problem Statement'''
#Read in first two chapters
    #Replace all hyphens with spaces
    #Remove all: "!"#$%&'()*+,./:;<=>?@[\]^_`{|}~"
        #import string
        #string.punctuation
            #to get a string of above punctuation, which includes hyphen.
    #Replace all uppercase letters with their lowercase equivalents
        #my_string.lower()
#Give two options
    #1. output the number of occurances of given word
    #2. Output the number of words that have specific legnth and then
    #count the unique words of that same length
        #my_list.count()


#reading in file
f = open("Pride&Prejudice_Ch1&2.txt", "r")
words = f.read()
f.close()

#do file stuff here
words = words.replace("-", " ")
words = words.translate(str.maketrans('', '', string.punctuation))
words = words.lower()

split_list = words.split()

print("Would you like to print the number of times a specific word appers OR print the number of words of a specific length? (1 or 2)")
choice = int(input("CHOICE> "))
if choice == 1:
    word = input("WORD> ")

    word = word.lower()
    
    count_words = 0
    for i in split_list:
        if i == word:
            count_words += 1
    
    print(f'The number of times {word} appears in the document is:')
    print(f'OUTPUT {count_words}')

elif choice == 2:
    print("Enter a length:")
    length = int(input("LENGTH> "))

    words_of_length = 0
    unique_words = []
    unique_words_count = 0
    for i in split_list:
        if len(i) == length:
            words_of_length += 1
            if i not in unique_words:
                unique_words.append(i)
                unique_words_count += 1

    print(f'The number of words in the document with length {length} is:')
    print(f'OUTPUT {words_of_length}')
        
    print(f'The number of unique words in the document with length {length} is:')
    print(f'OUTPUT {unique_words_count}')







    
