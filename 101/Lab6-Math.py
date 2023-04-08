#Addison Olstad
#CSCI 101 - Section C
#Python Lab 6
#References: None
#Time: 2 days


import csv
import math

def lilguy(equation):
    equation.remove('')
    valye = (len(equation) // 2)
    solution = 0
    if valye == 0:
        for i in equation:
            num = i
            num = num.strip()
            num = int(num)
        solution = num
    elif valye >= 1:
        for item in range(0, valye):
            one = equation.pop(0)
            operand = equation.pop(0)
            two = equation.pop(0)
            if operand == "+":
                cur_sol = float(one) + float(two)
                equation.insert(0, cur_sol)
            elif operand == "-":
                cur_sol = float(one) - float(two)
                equation.insert(0, cur_sol)
            elif operand == "*":
                cur_sol = float(one) * float(two)
                equation.insert(0, cur_sol)
            elif operand == "**":
                cur_sol = float(one) ** float(two)
                equation.insert(0, cur_sol)
            elif operand == "/":
                cur_sol = float(one) / float(two)
                equation.insert(0, cur_sol)
            elif operand == "%":
                cur_sol = float(one) % float(two)
                equation.insert(0, cur_sol)
        solution = int(round(cur_sol, 0))
            
    return solution

print("Enter the name of the file containing the math problems.")
mathfile = input("MATHFILE> ")
print("Enter the name of the file in which to store the results.")
outputfile = input("OUTPUTFILE> ")

with open(mathfile, 'r') as math, open(outputfile, 'w', newline='') as parsed_file:
    equations = math.readlines()
    writer = csv.writer(parsed_file)
    answers = []
    for i in range(0,len(equations)):
        temp = []
        equation = equations[i]
        equation = equation.split('==')
        print(equation)
        temp1 = equation[0]
        temp2 = equation[1]
        temp1 = temp1.split(',')
        temp2 = temp2.split(',')
        temp1_sol = lilguy(temp1)
        temp.append(temp1_sol)
        temp2_sol = lilguy(temp2)
        temp.append(temp2_sol)
        if temp1_sol == temp2_sol:
            temp.append("True")
        else:
            temp.append("False")
        answers.append(temp)


    #print(answers)

    for i in answers:
        writer.writerow(i)
        
