""" similar to the battleship_first script
but represents classes board and player used in battleship_second. This script is expected to be imported into
the battleship_second script"""
from random import randint
board = []


class Board(object):
    
	
    def __init__( self, board, number, size, ):
        self.board = []
        self.number = number
        self.size = size
		
        for item in range( self.size ):
            self.board.append( ["O"] * self.size )

    def get_size( self ):
        return self.size

    def get_board( self ):
        return self.board

#function creates the position of the ship on board
    def change_board_square( self,row,col,contents ):
        self.board[row][col] = contents

#random numbers generated for the ship position 
    def hidden_ship_position( self ):
        ship_row = randint( 0, (self.size) - 1 )
        ship_col = randint( 0, (self.size) - 1 )
        # the random values generated for the ship are printed
        #print( "Board %d Ship Column: %d" % ( self.number, ship_col ) )
        #print( "Board %d Ship Column: %d" % ( self.number, ship_row ) )
        return ship_row, ship_col



#The board is displayed to players
    def show_board( self ):
        print( "Board: %d" % self.number )
        for row in self.board:# columns within each row are fused together
            print( ' '.join( row ) )
"""
board1=[]
board_one = Board(board, 1, 5)
"""

class Player( object ):
    
    def __init__( self, player_name, board, number, size ):
        self.player_name = player_name
        self.number = number
        self.player_board = Board(board, number, size ) #gets values from the Board class To define board in player class

    def guess_ship( playa, ship_row, ship_col ):

      
    #4a. Compares guess values with randomly generated values
        #print_board(board)
        
        
        print( "The board shows your previous guess(es)" )
        playa.player_board.show_board()
    #4b. Collects guess values of battleship position from player
        guess_row = int( input( "%s Please guess a row number:" % ( playa.player_name ) ) )# receives guessed row number from player. {}.format(name)
        guess_col = int(input("Also guess a column number: "))# receives guessed column number from player

        win = guess_row == ship_row and guess_col == ship_col

        
        
            
                
            # conditions whereby the player looses
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4): # Case whereby player guesses out of range
            print("Oops, %s, that's not even in the ocean." %(playa.player_name))
            
        elif (playa.player_board.board[guess_row][guess_col] == "X"): #Case where player repeats previous guess.
            print("%s, You guessed that one already."%(playa.player_name))
            

            
        elif guess_row != ship_row or guess_col != ship_col: #case whereby player's guess is wrong and not one of the two cases above
            print( "%s, You missed the battleship!"%(playa.player_name))
            playa.player_board.change_board_square( guess_row, guess_col, "X" )
            #player_board.board[guess_row][guess_col]= "X"
            #board.get_board()[guess_row][guess_col] = "X"
        
        
         
        else:
            #if guess_row == ship_row and guess_col == ship_col: # Condition where player wins
            print("Congratulations! You sunk the battleship!")
            return 1

"""player_one = Player('Joe', board, 1, 5),
player_one.number
player_one.player_board.show_board()


                
board_one = Board(board1, 1, 5 )
board_two = Board(board2, 2, 5 )

board_one.show_board()
board_two.show_board()

player1 = Player( "Joe", board_one )
player2 = Player ("Mary", board_two)
        """


