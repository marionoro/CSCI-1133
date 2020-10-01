import math
import random
import turtle

# Creates an empty 8x8 board.
def createboard():
    turtle.speed(0)
    turtle.setworldcoordinates(0,0,9,9)
    turtle.penup()
    for a in range(1,9):
        turtle.goto(a,8.5)
        turtle.write(str(a-1), align = 'center', font = ("Arial", 12, "normal"))
    for b in range(1,9):
        turtle.goto(0.25, b)
        turtle.write(str(8-b), align = 'center', font = ("Arial", 12, "normal"))
    turtle.shapesize(2.75,2.75,2.75)
    turtle.shape("square")
    turtle.color("green")
    for i in range(1,9):
        for j in range(1,9):
            turtle.goto(i,j)
            turtle.stamp()

# Creates a token of given color.
def createtoken(color):
    turtle.speed(0)
    turtle.shape("circle")
    turtle.color(color)
    turtle.shapesize(2.75,2.75,2.75)
    turtle.stamp()

# Translates coordinates from matrix format to actual turtle x and y coordinates.
def coordinatetranslator(row,col):
    xval = col + 1
    yval = 8 - row
    return (xval, yval)

# Places a token of given color at a given location in the matrix.
# color is a numeric variable (1=black, 2=white)
def placetoken(color, input1, input2):
    turtle.speed(0)
    if color == 1:
        stringcolor = 'black'
    else:
        stringcolor = 'white'
    turtle.penup()
    coordinates = coordinatetranslator(input1, input2)
    turtle.goto(coordinates)
    createtoken(stringcolor)

# Creates the board at the beginning of the Othello game.
# color is a numeric variable (1=black, 2=white)
def createstartboard():
    turtle.speed(0)
    createboard()
    placetoken(1, 3, 4)
    placetoken(1, 4, 3)
    placetoken(2, 3, 3)
    placetoken(2, 4, 4)

# A function that finds all tokens of opposite color neighboring a given position on the board.
# the tupples in opponenttokens are (x,y, up/neutral/down, right/neutral/left)
# color is a numeric variable (1=black, 2=white)
def findopponentneighbors(board, row, col, color):
    opponenttokens = []
    if color == 1:
        opposite = 2
    else:
        opposite = 1
    for i in range(max(0,row-1), min(row+2, len(board))):
        for j in range(max(0,col-1), min(col+2, len(board))):
            if board[i][j] == opposite:
                opponenttokens.append((i, j, i - row, j - col))
    return opponenttokens

# Determines if a given coordinate is a valid move for the given color.
# color is a numeric variable (1=black, 2=white)
# the tupples in opponenttokens are (x,y, up/neutral/down, right/neutral/left)
def isValidMove(board,row,col,color):
    if color == 1:
        opposite = 2
    else:
        opposite = 1
    if board[row][col] != 0:
        return False
    neighbors = findopponentneighbors(board, row, col, color)
    for m in range(len(neighbors)):
        z = opposite
        x1 = neighbors[m][0]
        y1 = neighbors[m][1]
        while z == opposite and x1 in range(len(board)) and y1 in range(len(board)):
            z = board[x1][y1]
            x1 += neighbors[m][2]
            y1 += neighbors[m][3]
        if z == color:
            return True
    return False

# Finds a token of same color separated by a straight line of opposing tokens.
def findsamecolorinline(board, row, col, color):
    if color == 1:
        opposite = 2
    else:
        opposite = 1
    tokens = []
    neighbors = findopponentneighbors(board, row, col, color)
    for m in range(len(neighbors)):
        z = opposite
        x1 = neighbors[m][0]
        y1 = neighbors[m][1]
        while z == opposite and x1 in range(len(board)) and y1 in range(len(board)):
            z = board[x1][y1]
            if z == color:
                tokens.append((x1, y1))
            x1 += neighbors[m][2]
            y1 += neighbors[m][3]
    return tokens

# Creates a list of all valid moves for the given color.
# color is a numeric variable (1=black, 2=white)
def getValidMoves(board, color):
    validmoves = []
    for i in range(len(board)):
        for j in range(len(board)):
            if isValidMove(board, i, j, color):
                validmoves.append((i,j))
    return validmoves

# Selects the computer player's next move by randomly choosing a valid move.
def selectNextPlay(board):
    moves = getValidMoves(board, 2)
    if len(moves) == 0:
        return
    return moves[random.randint(0, len(moves)-1)]

# Creates a matrix representing the token placements at the beginning of the game.
# For the color of tokens, 1 = black and 2 = white.
def createstartmatrix():
    matrix = []
    for i in range(8):
        row = []
        for j in range(8):
            row.append(0)
        matrix.append(row)
    matrix[3][4] = 1
    matrix[4][3] = 1
    matrix[3][3] = 2
    matrix[4][4] = 2
    return matrix

# Determines which tokens should be created or flipped with a given token placement
def placements(board, row, col, color):
    mylist = [(row,col)]
    tokens = findsamecolorinline(board, row, col, color)
    for i in range(len(tokens)):
        xdif = tokens[i][0] - row
        ydif = tokens[i][1] - col
        xchange = int(xdif / max(abs(xdif), abs(ydif)))
        ychange = int(ydif / max(abs(xdif), abs(ydif)))
        a = row + xchange
        b = col + ychange
        for i in range(max(abs(xdif),abs(ydif))-1):
            mylist.append((a,b))
            a += xchange
            b += ychange
    return mylist

# Counts the number of black and white tokens on the board.
def tokencount(board):
    blackcount = 0
    whitecount = 0
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 1:
                blackcount += 1
            elif board[x][y] == 2:
                whitecount += 1
    return(blackcount, whitecount)

# For the color of tokens, 1 = black and 2 = white.
def main():
    turtle.speed(0)
    board = createstartmatrix()
    createstartboard()
    possibleblackmoves = getValidMoves(board, 1)
    possiblewhitemoves = getValidMoves(board, 2)
    while len(possibleblackmoves) != 0 or len(possiblewhitemoves) != 0:
        if len(possibleblackmoves) != 0:
            mystring = turtle.textinput('Your Next Move', 'Enter (Row, Col): ')
            endvar = 0
            if mystring == '':
                endvar = 1
                break
            coordinates = eval(mystring)
            while coordinates not in possibleblackmoves:
                mystring = turtle.textinput('INVALID CHOICE', 'Enter (Row, Col): ')
                if mystring == '':
                    endvar = 1
                    break
                coordinates = eval(mystring)
            if endvar == 1:
                break
            newblacktokens = placements(board, coordinates[0], coordinates[1], 1)
            for x in range(len(board)):
                for y in range(len(board)):
                    if (x,y) in newblacktokens:
                        board[x][y] = 1
                        placetoken(1, x, y)
            possiblewhitemoves = getValidMoves(board, 2)
        else:
            possiblewhitemoves = []
        if len(possiblewhitemoves) != 0:
            coordinates = selectNextPlay(board)
            newwhitetokens = placements(board, coordinates[0], coordinates[1], 2)
            for x in range(len(board)):
                for y in range(len(board)):
                    if (x,y) in newwhitetokens:
                        board[x][y] = 2
                        placetoken(2, x, y)
            possibleblackmoves = getValidMoves(board, 1)
        else:
            possibleblackmoves = []
    finalcount = tokencount(board)
    turtle.hideturtle()
    if endvar == 1:
        turtle.color("red")
        turtle.goto(2.5,0)
        turtle.write("PREMATURELY TERMINATED", align = 'center', font = ("Arial", 8, "normal"))
    turtle.color("black")
    turtle.goto(6,0)
    if finalcount[0] == finalcount[1]:
        turtle.write(("It's a tie! {0}-{1}".format(finalcount[0],finalcount[1])), align = 'center', font = ("Arial", 14, "normal"))
    elif finalcount[0] > finalcount[1]:
        turtle.write(("Congratulations! You won {0}-{1}".format(finalcount[0],finalcount[1])), align = 'center', font = ("Arial", 14, "normal"))
    else:
        turtle.write(("Sorry! You lost {1}-{0}".format(finalcount[0],finalcount[1])), align = 'center', font = ("Arial", 14, "normal"))


if __name__ == '__main__':
    main()
