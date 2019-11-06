class Board():
   def __init__(self, board,move):
       self.board = board
       self.move = move
    
   def  DrawBoards(self,board):
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' +self.board[4] + ' | ' +self.board[5] + ' | ' +self.board[6])
        print('   |   |')     
        print('-----------')
        print('   |   |')
        print(' ' +self.board[1] + ' | ' +self.board[2] + ' | ' +self.board[3])
        print('   |   |')
    
   def getBoardCopy(self,board):
        fakeBoard = [""]
        for i in self.board:
                fakeBoard.append(i)
        return fakeBoard
   
   def isBoardFull(self,board):
        for i in range(1,10):
            if self.board[i] == " ":
                return False
        return True
    
   def isSpaceFree(self,board,move):
         return board[move] == " "
   
   