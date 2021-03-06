"""Battleship game that makes use of the Board class   """

from random import randint

import battleship1

board_size =int(input("Enter the size of the board you want to use: " ) )
max_turns  = 0
no_of_players = 0   

while max_turns <= 0:
    try:

        max_turns = int(input("Enter the maximum number of game turns: " ))
        
    except ValueError:
        print( "Please enter a number!" )
    if max_turns < 0 :
        print("Enter a positive integer" )
    


while no_of_players < 2:
    
    try:

        no_of_players = int( input( "Enter the number of players: " ) )# requests the name of the player

    except ValueError:
        print( "Please enter a number!" )
    if no_of_players < 2:
        
        print( "Please type a value greater than 1!" )
    




 



#"player2 = ( input( "Enter the name of the second player: ") )
#"player3 = ( input( "Enter the name of the third player: ") )


                
hidden_ship = battleship1.Board( [], 0, board_size )
hidden_ship.hidden_ship_position()
ship_row, ship_col = hidden_ship.hidden_ship_position()
print( ship_row, ship_col )

winners = []
player_names = []
player_class_names = []
player_classes = []

for i in range ( 1, (no_of_players + 1) ):
    
    player_name = input( "Enter player %s: " % ( i )  )

    player_names.append( player_name )

    player_class_name = "player" + str(i)
    player_class_names.append( player_class_name)

    player_class_names[i-1] = battleship1.Player( player_name, [], i, board_size )

    player_classes.append( player_class_names[i-1])



"""        
player_one = battleship1.Player( player1, [], 1, board_size )
player_two = battleship1.Player( player2, [], 2, board_size )
player_three = battleship1.Player( player3, [], 3, board_size )

players = [player_one, player_two, player_three]"""

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
        eplayer1_gameit() 
    else:
    # conditions whereby the player looses
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4): # Case whereby player guesses out of range
            print("Oops, %s, that's not even in the ocean." %(playa.player_name))
        elif (playa.player_board.board[guess_row][guess_col] == "player1_game"): #Case where player repeats previous guess.
            print("%s, You guessed that one already."%(playa.player_name))
        else: #case whereby player's guess is wrong and not one of the two cases above
            print( "%s, You missed the battleship!"%(playa.player_name))
            playa.player_board.change_board_square( guess_row, guess_col, "X" )
            #player_board.board[guess_row][guess_col]= "X"
            #board.get_board()[guess_row][guess_col] = "X"
            
                
 """               
current_player_index = 0 # starting player
"""
def next_player_index( no_of_players):
    if turn % 2 == 1:
        return 1
    else:
        return 0
        """

        
"""
turn % 2 = 0 means player 2
turn % 2 = 1 means player 1
input odd, intended output player1, actual output:
input even, intended output , actual output : 
"""


for game_turn in range( 1,( max_turns + 1) ):
    
    print( "Turn", game_turn )
             
    for player_class in player_classes:
        
        active_player = battleship1.Player.guess_ship( player_classes[ current_player_index ], board_size, ship_row, ship_col )
    
        if active_player == True:

            winners.append( player_classes[ current_player_index ].player_name )
        
            player_classes.remove( player_classes[ current_player_index ])

            if player_classes == []:

                print( "The game is draw!" )

                break

            else:
                current_player_index = ( ( current_player_index ) % len( player_classes ))
            
        else:
            current_player_index = ( ( current_player_index +1 ) % len( player_classes ))

    

    if game_turn == ( max_turns ):

        print( "Game Over!" )

    #player2_game = battleship1.Player.guess_ship( players[ current_player_index ], ship_row, ship_col )
    
    #current_player_index = ( ( current_player_index +1 ) % 3 )
    
    #player3_game = battleship1.Player.guess_ship( players[ current_player_index ], ship_row, ship_col )
    
    #current_player_index = ( ( current_player_index +1 ) % 3 )
 
    #current_player_index = ( ( current_player_index +1 )% 3 ) #
    #current_player_index = next_player_index( turn )
    #battleship1.Player.player_guess_count( players[ current_player_index ] )
"""
    if (  player1_game == player2_game == player3_game == True ) or ( player1_game == player2_game == True ) or ( player2_game == player3_game == True ) or ( player1_game == player3_game == True ):
        print( "Game Over! It's a draw" )
        break
    elif ( player1_game == True ) and ( player2_game == player3_game == False ):
        print("Game Over!: %s has won the game" %( player1 ) )
        break
    elif ( player2_game == True ) and ( player1_game == z ==  False):
        print( "Game Over!: %s has won the game" %( player2 ) )

    elif ( player3_game == True ) and ( player1_game == player2_game == False):
        print( "Game Over!: %s has won the game" %( player3 ) )
        break """
    
    
    





"""
record the right position of the ship on player boards

player_boards = [board_one, board_two]
player_boards[1]
player_boards[1].board[guess_row][guess_col] == "player1_game"

"""

for player_class in player_classes:

    player_class.player_board.change_board_square( ship_row, ship_col, "A" )# create an instance of the hidden ship

    print("%s guesses:" %( player_name ))

    player_class.player_board.show_board()

"""                             
#rint(ship_row,ship_col)
player_one.player_board.change_board_square( ship_row, ship_col, "A" )# in the firt player board, create an instance of the hidden ship.
#rint(player_one.player_board.board[ship_row][ship_col])
rint("%s guesses:" %( player1 ))
player_one.player_board.show_board() #display the first player board containing the missed values of the ship


#displaying hidden ship on the second player's board
player_two.player_board.change_board_square(ship_row, ship_col, "A")# in the second player board, create an instance of the hidden ship.

#print(player_two.player_board.board[ship_row][ship_col]) # Print the hidden ship on the board
print("%s guesses:" %( player2 ))
player_two.player_board.show_board() #display the second player board containing the missed values of the ship

#displaying hidden ship on the second player's board
player_three.player_board.change_board_square(ship_row, ship_col, "A")# in the second player board, create an instance of the hidden ship.

#rint(player_two.player_board.board[ship_row][ship_col]) # Print the hidden ship on the board
rint("%s guesses:" %( player3 ))
player_three.player_board.show_board() #display the third player board containing the missed values of the ship

"""






#Display the actual value of the ship's position when game is over.
           


print( "The ship's position is: " "row %s, column %s (represented with letter \' A \' on each board)"  % (ship_row, ship_col))            
print( "The winners are:" )

if winners == []:
    print(" You all lost!")

else:
    print( ', '.join(winners))

