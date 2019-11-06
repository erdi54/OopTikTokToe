from Board import *
import random

class Move(Board):

    def __init__(self,board,move,letter):
        super(Move, self).__init__(board,move)
        self.letter= letter
        


    def getPlayerMove(self):
        
        while self.move not in '1 2 3 4 5 6 7 8 9'.split() or not self.board[int(self.move)] == " ":
            print("What is your next move? (1-9)")
            self.move = input()
            
        return int(self.move)
    
    def getComputerMove(self,board,computerLetter):
        move = 0
        if computerLetter == "X":
            playerLetter = "O"
        else:
            playerLetter =  "X"

        for i in range(1,10):
            
            copy =Board.getBoardCopy(self,board)
           
            if Board.isSpaceFree(self,copy,i):
                self.makeMove(copy, i ,computerLetter)
                if self.isWinner(copy, playerLetter):
                    return i
                

        for i in range(1,10):
            copy = Board.getBoardCopy(self,board)
            if Board.isSpaceFree(self,copy, i):
                self.makeMove(copy, i,playerLetter )
                if self.isWinner(copy, playerLetter):  
                    return i
        move = self.chooseRandomMoveFromList(board,[1,3,7,9])  
        
        if move != None:
            return move
        
        if  board[5] == " ":
            return 5         
        
        return self.chooseRandomMoveFromList(board, [2,4,6,8])

    def chooseRandomMoveFromList(self,board, movesList):
        possibleMoves = []
        for i in movesList:
            if Board.isSpaceFree(self,board,i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None
    def makeMove(self, board,move,letter):
        board[move] =letter

    def isWinner(self,bo, le):
      return (  (bo[7] == le and bo[8] == le and bo[9] == le) or# üst kısımda
                (bo[4] == le and bo[5] == le and bo[6] == le) or# orta kısım
                (bo[1] == le and bo[2] == le and bo[3] == le) or# alt  kısım
                (bo[7] == le and bo[4] == le and bo[1] == le) or# sol taraftan
                (bo[8] == le and bo[5] == le and bo[2] == le) or#ortadan aşağıya
                (bo[9] == le and bo[6] == le and bo[3] == le) or#sağdan aşağıya
                (bo[7] == le and bo[5] == le and bo[3] == le) or#çapraz
                (bo[9] == le and bo[5] == le and bo[1] == le))#capraz# """  """
   
  

