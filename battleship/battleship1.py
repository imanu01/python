""" similar to the battleship_first script
but represents classes board and player used in battleship_second. This script is expected to be imported into
the battleship_second script"""
board = []


class Board(object):
    
	
    def __init__( self, board, number, size, ):
        self.board = []
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
"""
board1=[]
board_one = Board(board, 1, 5)
"""

class Player( object ):
    
    def __init__( self, player_name, board, number, size ):
        self.player_name = player_name
        self.number = number
        self.player_board = Board(board, number, size ) #gets values from the board class
"""        
player_one = Player('Joe', board1, 1, 5)
player_one.number
player_one.player_board.show_board()


"""		
board_one = Board(board1, 1, 5 )
board_two = Board(board2, 2, 5 )

board_one.show_board()
board_two.show_board()

player1 = Player( "Joe", board_one )
player2 = Player ("Mary", board_two)

"""
