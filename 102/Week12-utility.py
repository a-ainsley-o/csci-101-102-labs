#Addison Olstad
#CSCI 102 - Section C
#Assessment 12C
#References:
#Time:

def load_file(filename):
    lines = filename.splitlines()
    print("OUTPUT", lines)

def update_string(string1, string2, integer):
    str_1_lines = list(string1)
    str_1_lines[integer] = string2
    empty_str = ""
    for i in str_1_lines:
        empty_str += i
    print("OUTPUT", empty_str)

def find_word_count(list1, string):
    num = list1.count(string)
    print(num)

def score_finder(list1, list2, string):
    if string in list1:
        num = list1.index(string)
        score = list2[num]
        print("OUTPUT", list1[num], "got a score of", score)
    else:
        list1 = list(map(str.lower,list1))
        if string in list1:
            num = list1.index(string)
            score = list2[num]
            print("OUTPUT", list1[num], "got a score of", score)
        else:
            print("OUTPUT player not found")

def union(list1, list2):
    list3 = list1 + list2
    print(list3)

def intersect(list1, list2):
    list3 = []
    for i in list1:
        if i in list2:
            list3.append(i)
    print(list3)

def not_in(list1, list2):
    list3 = []
    for i in list1:
        if i not in list2:
            list3.append(i)
    print(list3)

def is_prime(integer):
    if integer <= 1:
        print("False")
    elif integer == 2:
        print("True")
    else:
        for i in range(2, integer):
            if (integer % i) == 0:
                return print("False")
        return print("True")









    
