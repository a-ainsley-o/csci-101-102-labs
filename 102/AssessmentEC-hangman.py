#Addison Olstad
#CSCI 102- Section H
#Assessment EC
#References:
#Time: literally my entire life


#entry prompting info
print("Welcome to simple Hang Man")
print("Enter a secret word:")
sec_word = input("WORD> ")
print("Enter the number of guesses allowed:")
num_gues = int(input("NUM> "))
char_list = []

#function that changes unknown word as player guesses
#ISSUE: List changes each time, doesn't append.

cur_state = list('_' * len(sec_word))
print(cur_state)

#While number of guesses is above 0
char_gues = ""
while num_gues > 0:
    
    print("Please enter a character: ")
    temp_gues = input("CHAR> ")
    char_gues += temp_gues
    
    if char_gues in char_list:
        
        print("OUTPUT Boo! You guessed incorrectly!")
        num_gues -= 1
        
        if num_gues == 1:
            print(f'{num_gues} guess remaining')
            
        else:
            print(f'{num_gues} guesses remaining')
            
        print("Character's guessed:", end = ' ')
        print(char_list)
        #enter cur_stat with update
    
    else:
        char_list.append(temp_gues)
        num_gues -= 1
        if temp_gues == sec_word:
            print("OUTPUT Congratulations! You guessed the secret word!")
            if num_gues == 1:
                print(f'{num_gues} guess remaining')
            else:
                print(f'{num_gues} guesses remaining')
            print("Character's guessed:", end = ' ')
            print(char_list)
            print(f'OUTPUT {sec_word}')
            break
        elif temp_gues in sec_word:
            for i in range(0, len(sec_word)):
                if "_" != cur_state[i]:
                    break
                else:
                    for j in range(0, len(sec_word)):
                        if temp_gues == sec_word[j]:
                            if cur_state[j] == "_":
                                cur_state[j] = temp_gues
                                
            print("OUTPUT Success! You guessed a character in the word!")
            if num_gues == 1:
               print(f'{num_gues} guess remaining')
            else:
                print(f'{num_gues} guesses remaining')
            print("Character's guessed:", end = ' ')
            print(char_list)
            #update cur_state, gonna index the sec_word with where temp_gues is, then replace that index in cur_stat with temp_gues
            k = sec_word.index(temp_gues)
            print(k)
            #cur_state[k] = temp_gues
            print(' '.join(cur_state))
        elif temp_gues not in sec_word:
            if num_gues == 0:
                break
            print("OUTPUT Boo! You guessed incorrectly.")
            if num_gues == 1:
                print(f'{num_gues} guess remaining')
            else:
                print(f'{num_gues} guesses remaining')
            print("Character's guessed:", end = ' ')
            print(char_list)
                
if num_gues <= 0:
    print("OUTPUT You ran out of guesses! Better luck next time!")
    print(f'OUTPUT secret word {sec_word}')
    
                


