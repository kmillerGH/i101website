#Final Assignment
import random

#Global Constants
TOPSCORES = 5
BOARD = 121
W = 11 #11 by 11 board
D = "v" #+11 Red/R
U = "^" #-11 Yellow/Y
L = "<" #-1 Blue/B
R = ">" #+1 Green/G

#Global Variables

#Functions
#10 points- Answer the following questions in your submission file and comment them out.
def createBoard():
    """Creating the board with numbers from 0-BOARD"""

    """Think about it: Can you simplify this code?"""
    board = []

    for square in range(BOARD):
        #1 Explain (2)
        #This line adds an item to the list 'board'.  The item is a list of the number, a blank space and a 0.
        #It will be used later in the program to create the board.
        board.append([square," ",0])

        #2 Explain what is [square, U, -11] or [square, R, 1] for example. (2)
        #The if and elif statements create the board arrows.  The list item [square, U, -11] has three parts.
        #The square is the index position number of the spot.  The letter represents the direction of the arrow.
        #For this item, a '^' will be placed because it is a U (up).
        #The -11 represents the vertical position of the space.
        #3 What are the numbers of the square targeted by "if square%11 == 4 and square > 4" (2)
        #The numbers are 15, 26,37, 48, 59, 70, 81, 92, 103, 114.  However, the next if statement removes the numbers
        #48, 59, 70 because they are in the center of the board.
        if square%11 == 4 and square > 4:
                board[square] = [square,U,-11]
        elif square%11 == 5:
            if square <= 49:
                board[square] = [square,D,11]
            else:
                board[square] = [square,U,-11]
                
        if square%11 == 6:
                board[square] = [square,D,11]

        if square >= 44 and square < 60 and square != 48 and square != 49:
            board[square] = [square, R, 1] 
        elif square > 60 and square < 77 and square!=71 and square != 72:
            board[square] = [square, L, -1]

        #3 Explain why these are necessary (2)
        #These lines are at the edges of the playing space.  The following statements change the arrows so that the board
        #can loop all the way around.  For example, square 4 was intially pointing up, but the first if statement changes
        #it to face right so the player does not go of he board.
        if square == 4 or square == 5:
            board[square] = [square, R, 1]
        elif square == 54 or square == 65:
            board[square] = [square, D, 11]
        elif square == 66 or square == 55:
            board[square] = [square, U, -11]
        elif square == 116 or square == 115:
            board[square] = [square, L, -1]

    #4 Explain what these positions mean (2)
    #These positions are unique spots on the board.  The first four are starting places for each player.
    #The letters represent colors. R=red, B= blue, Y=yellow, G=green.
    #board[60] is the center of the board. This is where players end up.
    #The third item in these lists is the vertical position of the spot.  For example, 'R' is 11 rows above the center.
    board[6] = [6, "R", 11]
    board[76] = [76, "B", -1]      
    board[114] = [114, "Y", -11]      
    board[44] = [44, "G", 1]      
    board[60] = [60, "C"]
            
    return board

#10 points
def saveScore(curscore):
    try:
        text_file = open("score.txt", "a")
        read
        for item in scorelist:
            text_file.write("%s\n" % item)
    except:
        print("Something went wrong!")
    text_file.close()
    """
    Save the top 5 scores in the score.txt file

    score.txt should contain only a list of numbers sorted in ascending order (small to big)
   
    Use try and except for file open and close (2 points)
    """

#5 points
def showScore():
    try:
        text_file = open("score.txt", "r")
        print(text_file)
    except IOError as e:
        print(e)
    text_file.close()
    """
    Read the score.txt file and print the scores to the screen

    Use try and except for file open and close (1 point)

    """

#10 points
def printBoard(board):
    loop = 0
    for i in range(len(board)):
        loop += 1
        if loop > 11:
            loop -= 11
            print("\n----------------------")
        print(board[i][1],end='|')

    
#2 points
def roll_die(player):
    roll = random.randrange(0,7)
    print("You rolled a", roll)
    return roll

#10 points
def validMove(player,tokenPos,pHomePos,roll,board):
    if tokenPos == 0:
        if roll == 6:
            return pStartPos
        else:
            return 'N'
    else:
        pathlocation += roll
        tokenPos = bluepath[pathlocation]
        return pathlocation
        
    """This function determines if the move on the board is valid and returns the new token position

    1) If the token is at the entrance of the home of the player, determine the new token
    position and return it (3)
    2) If the token is not at the entrance, then it's a regular move. Determine the new token position
    and return it (3)
    3) If the token is in the center of the board, but the roll is not complete, then don't move. Ask the
    user to roll again. Return the current position as your new token position (3)

    Repeat the above process roll times i.e. if roll is six, player will move six positions on the board
    and above process has to repeat six times (1)

    Position here refers to the square number on the board e.g 65, 78
    """ 

#23 points
def playGame(board):

    """Start writing the game with a single player. The following
    variables and descriptions are set up for a single player game. You will have to
    modify them for multiple player game.
    """
    print("\n\nThis version of Ludo involves two players.  The goal of the game is to reach the middle of the board in the least number of moves.")
    print("To get onto the board, a player must roll a 6.  Once their token is on the board, the player recieves 25 points.")
    print("A player recieves 1 point for each move on the board.  If Player 1's token lands on the same spot as Player 2's token, Player 2 gets bounced off the board.")

    bluepath = {0:76,1:75,2:74,3:73,4:72,5:83,6:94,7:105,8:116,9:115,10:114,11:103,12:92,13:81,14:70,15:69,16:68,17:67,18:66,19:55,20:44,21:45,22:46,23:47,24:48,25:37,26:26,27:15,28:4,29:5,30:6,31:17,32:28,33:39,34:50,35:51,36:52,37:53,38:54,39:65,40:64,41:63,42:62,43:61,44:60}

    player = 1 #which player
    pStartPos = 76 
    pHomePos = 65 #the entry square position of the home of the player
    tokenPos = 0 #same as board position with three items
    tokenSym = "X" #token symbol of each player
    score = 0 
    roll = 0
    pathlocation = 0
    
    loop = 0
    while loop < 1:
        ask = input("\n\nType r to roll:")
        score += 1
        if ask == "r":
            roll = roll_die(player)
            if roll == 6:
                tokenPos = 0
                tokenPos = bluepath[pathlocation]
                board[tokenPos] = [tokenPos, tokenSym, -1]
                printBoard(board)
                score += 25
                loop += 1
            else:
                print("A six is needed to start, roll again")

    loop = 0
    while loop < 1:
            ask = input("\n\nType r to roll:")
            if ask == "r":
                roll = roll_die(player)
                score += 1
                ##pathlocation += roll
                pathlocation += 44
                if pathlocation >= 44:
                    print("Congratulations, you've won!")
                    print("Your score is", score)
                    saveScore(score)
                    showScore()
                    loop += 1
                else:
                    board[76] = [76, "B", -1]
                    tokenPos = bluepath[pathlocation]
                    origspace = board[tokenPos]
                    board[tokenPos] = [tokenPos, tokenSym, -1]
                    printBoard(board)
                    board[tokenPos] = origspace
            else:
                print("Invalid input")
                ask = input("\n\nType r to roll:")



##    while true:
##        roll=roll_die()
##        newpos = validMove(p, tokenPos, pHomepos, roll, board)
##        if newpos != 'N'
    """
        (10 points)
        Ask Player to press r to roll the dice

        If the token of the player is not on the board i.e. token position is still 0 and the roll is
        not six, ask player to roll again

        If the token of the player is not on the board and the roll is six, place the token at the start
        position and let the player roll again

        If token of the player is on the board i.e. token position is not 0, then make a move.
            Call validMove
            Make the move based on what validMove returns
            When making a move from board position 1 to board position 2, replace the
            original value of board position 1 and update board position 2. These positions refer to
            the position as a list.

        If token of the player is at the center of the board, then tokenPos of the player should be empty
         
        Repeat the process above while tokenPos of the player is not an empty list (game ends)

        When game ends,
        Print the score
        Call saveScore
        Call showScore

        Print Feedback (3 points)
        --------------
        Print messages on the screen to inform the player. Think of what kind of messages would
        be useful for someone who has no idea how your game works.

        Multiple Players (10 points)
        ----------------
        For two players, you have to decide who starts the game and switch players
        when appropriate.(5)
        If player 1's token lands on player 2 's token position, then player 2 token
        should be kicked off the board i.e. player 2's token position should be set to [0,0,0]
        and the game continues...
        (5)
        """
    
def main():
    board = createBoard()
    printBoard(board)
    playGame(board)

main()
