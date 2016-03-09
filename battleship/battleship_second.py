"""Battleship game that makes use of the Board class   """

from random import randint

import battleship1
board = []

#2. Designing the boards for the Game




#board = battleship1.Board( board, 0, board_size )


max_guesses = int(input("Enter the maximum number of guesses you want to play: " ))
    
player1 = ( input( "Enter the name of the first player: " ) )# requests the name of the player
player2 = ( input( "Enter the name of the second player: ") )

board_size =int(input("Enter the size of the board you want to use: " ) )
                
hidden_ship = battleship1.Board( board,0,board_size )
hidden_ship.hidden_ship_position()
ship_row, ship_col = hidden_ship.hidden_ship_position()
print( ship_row, ship_col )




        
player_one = battleship1.Player( player1, board, 1, board_size )
player_two = battleship1.Player( player2, board, 2, board_size )
players = [player_one, player_two]

"""
def guess_ship(playa, ship_row, ship_col ):

  
#4a. Compares guess values with randomly generated values
    #print_board(board)
     
    print("The board shows your previous guess(es)")
    playa.player_board.show_board()
#4b. Collects guess values of battleship position from player
    guess_row = int(input("%s Please guess a row number:" % (playa.player_name)))# receives guessed row number from player. {}.format(name)
    guess_col = int(input("Also guess a column number: "))# receives guessed column number from player

    if guess_row == ship_row and guess_col == ship_col: # Condition where player wins
        print("Congratulations! You sunk the battleship!")
        exit() 
    else:
    # conditions whereby the player looses
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4): # Case whereby player guesses out of range
            print("Oops, %s, that's not even in the ocean." %(playa.player_name))
        elif (playa.player_board.board[guess_row][guess_col] == "X"): #Case where player repeats previous guess.
            print("%s, You guessed that one already."%(playa.player_name))
        else: #case whereby player's guess is wrong and not one of the two cases above
            print( "%s, You missed the battleship!"%(playa.player_name))
            playa.player_board.change_board_square( guess_row, guess_col, "X" )
            #player_board.board[guess_row][guess_col]= "X"
            #board.get_board()[guess_row][guess_col] = "X"
            
                
 """               
current_player_index = 0 # starting player
"""
def next_player_index( turn ):
    if turn % 2 == 1:
        return 1
    else:
        return 0
        """
"""def player_guess_count( turn  ):
    player1_count = 0
    player2_count = 0
    for player1_count < max_guesses
        if next_player_index( turn ) == 1:
            player1_count = player1_count + 1
            if player1_count = max_guesses:
                print("You've used up all your guesses.")
    for
    elif next_player_index( turn ) == 0:
            player2_count = player2_count + 1
            if player1_count = max_guesses:
                print("You've used up all your guesses.")
"""
        
"""
turn % 2 = 0 means player 2
turn % 2 = 1 means player 1
input odd, intended output player1, actual output:
input even, intended output , actual output : 
"""


for turn in range( 1,( max_guesses + 1) ):
    
    print( "Turn", turn )
             
        
    Y = battleship1.Player.guess_ship( players[ current_player_index ], ship_row, ship_col )
    
    current_player_index = ( ( current_player_index +1 )% 2)
    Z = battleship1.Player.guess_ship( players[ current_player_index ], ship_row, ship_col )
    
    current_player_index = ( ( current_player_index +1 )% 2 )
    #current_player_index = ( ( current_player_index +1 )% 2 ) #0: 1, 1: 0
    #current_player_index = next_player_index( turn )
    #battleship1.Player.player_guess_count( players[ current_player_index ] )

    if ( Y == True ) and ( Z == True ):
        print( "Game Over! It's a draw" )
        break
    elif ( Y == True ) and ( Z == False ):
        print("Game Over!: %s won the game" %( players[ ( current_player_index+1 )% 2 ].player_name ) )
        break
    elif Y == False and Z == 1:
        print( "Game Over!: %s won the game" %( players[ current_player_index ].player_name ) )
        break
    
    if turn == ( max_guesses ):
        print( "Game Over!: None of you has won" )
    





"""
record the right position of the ship on player boards

player_boards = [board_one, board_two]
player_boards[1]
player_boards[1].board[guess_row][guess_col] == "X"

"""
#print(ship_row,ship_col)
player_one.player_board.change_board_square( ship_row, ship_col, "A" )# in the firt player board, create an instance of the hidden ship.
#print(player_one.player_board.board[ship_row][ship_col])
print("%s guesses:" %( player1 ))
player_one.player_board.show_board() #display the first player board containing the missed values of the ship


#displaying hidden ship on the second player's board
player_two.player_board.change_board_square(ship_row, ship_col, "A")# in the second player board, create an instance of the hidden ship.

#print(player_two.player_board.board[ship_row][ship_col]) # Print the hidden ship on the board
print("%s guesses:" %( player2 ))
player_two.player_board.show_board() #desplay the second player board containing the missed values of the ship









#Display the actual value of the ship's position when game is over.
           


print( "The ship's position is: " "row %s, column %s (represented with letter 'A' on each board)"  % (ship_row, ship_col))            


