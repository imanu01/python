""" similar to the battleship_first script
but represents classes board and player used in battleship_second. This script is expected to be imported into
the battleship_second script"""
board = []
board1 = []
board2 = []

class Board(object):
    
	
    def __init__( self, board, number, size, ):
        self.board = board
        self.number = number
        self.size = size
		
        for item in range( self.size ):
            self.board.append( ["O"] * self.size )

    def get_size(self):
        return self.size

    def get_board(self):
        return self.board

#The board is displayed to players
    def show_board( self ):
        print( "Board: %d" % self.number )
        for row in self.board:# columns within each row are fused together
            print( ' '.join( row ) )	

	
	

class Player( object ):
    
    def __init__( self, name, board ):
        self.name = name
        self.board = board
		
    def player_turns(self, player):
        if total_turns % 2 == 1:
            return player_one
        else:
            return player_two
"""		
board_one = Board(board1, 1, 5 )
board_two = Board(board2, 2, 5 )

board_one.show_board()
board_two.show_board()

player1 = Player( "Joe", board_one )
player2 = Player ("Mary", board_two)

"""
