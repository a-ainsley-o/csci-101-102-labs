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
