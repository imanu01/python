#Script of game called battleship for two players. 
"""This script has been written for a battleship game to be played by two people. In the game, a 5*5 matrix board is created.
The script randomly selects a position of a battleship by randomly generating a row and a column from the 5*5 matrix.
Players take turns to guess the position of the ship. The winner is the one whose guess corresponds to the randomly generated numbers.
Players input their guesses in an alternating manner.
Each player's wrong guess is displayed on a seperate board and presented to the player before each guess to avoid s/he repeating the guess.
At the beginning of the game, the players pre-determine the maximum number of guesses permitted before the game ends."""

#1. From the Random module, import a function for creating a random set of integers

from random import randint


#2. Designing the boards for the Game
board = []
board1 = []       
board2 = []  

# 2a. Creating a list of 5 lists to serve as game platform
for x in range(5): #range starts from 0 to 4
#list consisting of 5 "O" is appended into board 5 timescreating a list of 5 lists
    board.append(["O"]*5)
    board1.append(["O"] * 5) 
    board2.append(["O"]*5)
#print( board)
max_games = int(input("Enter the maximum number of games you want to play: " ))
    
player1 = (input("Enter the name of the first player: "))# requests the name of the player
player2 = (input("Enter the name of the second player: "))

players = [player1, player2]

#b. A function is created that fuses the lists into a 5 x5 matrix to serve as a gaming platform
def print_board(board):
    for row in board:
             
        print(" ".join(row))# Each row is fused in the board
                
def print_board1(board1):
    for row in board1:
              
        print(" ".join(row))# Each row is fused in the board

def print_board2(board2):

    for row in board2:
                
        print(" ".join(row))# Each row is fused in the board

turn = 1






#3. Creating Functions that Randomly Assign the Position of the Battleship

def random_row(board): # function for random row position of battleship
    return randint(0, len(board) - 1)

def random_col(board): # function for random column position of battleship
    return randint(0, len(board) - 1)

# Using functions to randomly assign position of battleship
ship_row = random_row(board)
ship_col = random_col(board)
#print(ship_row)
#print(ship_col)



#4. Function to Determine Outcome of Game by Players


    
def guess_ship(playa):

  
#4a. Collects guess values of battleship position from player 
    guess_row = int(input("%s Please guess a row number:" % (playa)))# receives guessed row number from player. {}.format(name)
    guess_col = int(input("Also guess a column number: "))# receives guessed column number from player

#4b. Compares guess values with randomly generated values
    #print_board(board)
    print("The board shows your previous guess(es)")
    if playa == player1:
        print_board1(board1)
    elif playa == player2:
        print_board2(board2)
    if guess_row == ship_row and guess_col == ship_col: # Condition where player wins
        print("Congratulations! You sunk the battleship!")
        exit() 
    else:
    # conditions whereby the player looses
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4): # Case whereby player guesses out of range
            print("Oops, %s, that's not even in the ocean." %(playa))
        elif (board[guess_row][guess_col] == "X"): #Case where player repeats previous guess.
            print("%s, You guessed that one already."%(playa))
        else: #case whereby player's guess is wrong and not one of the two cases above
            print( "%s, You missed the battleship!"%(playa))
            
            if playa == player1:
                board1[guess_row][guess_col] ="K"
                board[guess_row][guess_col] ="K"
                
            elif playa == player2:
                board2[guess_row][guess_col] ="J"
                board[guess_row][guess_col] ="J"
                
                
           
                
#5. Counting the number of turns to play



players = [player1, player2]
player = 0 # starting player 

for turn in range(max_games):
    turn = turn +1
    print("Turn", turn)
             
        
    guess_ship(players[player])
    player = ( ( player +1 )% 2) #0: 1, 1: 0

        
    if turn == max_games:
        print("Game Over!")
           
board[ship_row][ship_col] = "A"
print("%s guesses:" %(player1))
print_board1( board1 )
print("%s guesses:" %( player2 ))
print_board2( board2 )
print("Total guesses")
print_board(board)

print( "The ship's position is: " "row %s, column %s"  % (ship_row, ship_col))
#print(ship_row)
#print(ship_col)
