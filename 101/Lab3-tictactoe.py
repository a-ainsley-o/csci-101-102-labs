#Addison Olstad
#CSCI 101- Section C
#Python Lab 3
#References: None
#Time: 39 minutes

#creating a piece of code that analyzes the board and tells the players
#if anyone has won.

#inputs
row0 = str(input("ROW0> "))
row1 = str(input("ROW1> "))
row2 = str(input("ROW2> "))

def tictactoe(row0, row1, row2):
    #defining 
    winner = ""
    if (len(row0) == 3 and (row0[0] == "X" or row0[0] == "O" or row0[0] == "E")) and (len(row1) == 3 and (row1[0] == "X" or row1[0] == "O" or row1[0] == "E")) and (len(row2) == 3 and (row2[0] == "X" or row2[0] == "O" or row2[0] == "E")):
    
        #checking for row wins
        if row0 == "XXX" or row1 == "XXX" or row2 == "XXX":
            winner += "X"
        if row0 == "OOO" or row1 == "OOO" or row2 == "OOO":
            winner += "O"

        #checking for diagonal wins
        if (row0[0] == "X" and row1[1] == "X" and row2[2] == "X") or (row0[2] == "X" and row1[1] == "X" and row2[0] == "X"):
            winner += "X"
        if (row0[0] == "O" and row1[1] == "O" and row2[2] == "O") or (row0[2] == "O" and row1[1] == "O" and row2[0] == "O"):
            winner += "O"

        #checking for column wins
        if row0[0] == row1[0] and row0[0] == row2[0]:
            if row0[0] == "X":
                winner += "X"
            if row0[0] == "O":
                winner += "O"
        if row0[1] == row1[1] and row0[1] == row2[1]:
            if row0[1] == "X":
                winner += "X"
            if row0[1] == "O":
                winner += "O"
        if row0[2] == row1[2] and row0[2] == row2[2]:
            if row0[2] == "X":
                winner += "X"
            if row0[2] == "O":
                winner += "O"

        #for ties
        if winner == "":
            winner += "T"

    else:
        winner = "ERROR"

    return winner

print(f'OUTPUT {tictactoe(row0, row1, row2)}')
