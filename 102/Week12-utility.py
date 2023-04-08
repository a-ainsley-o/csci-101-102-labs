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
