from Player  import *
from Board import *
from Move import *

print("TikTakToe! Hoşgeldiniz")
 

while True:
   theBoard=[" "]*10
   Templetter = " "
   move = " "
   CreatBoard = Board(theBoard,move)
   CreatMove = Move(theBoard,move,Templetter)
   CreatPlayer = Player(Templetter)
   Templetter=CreatPlayer.inputPlayerLetter() 
   playerLetter= Templetter
   computerLetter= CreatPlayer.X_or_O(Templetter)
   if CreatPlayer.whoGoesFirst() == "computer":
       
        turn = "computer"
        
   else :
        turn ="player"  
        
    
   print ("ilk olarak "+ turn +" başlayacak")
    
   gameIsPlaying = True
   while gameIsPlaying:
        if turn== "player":
            CreatBoard.DrawBoards(theBoard)
            move = CreatMove.getPlayerMove()
            CreatMove.makeMove(theBoard,move,playerLetter)
            if CreatMove.isWinner(theBoard,playerLetter):
                CreatBoard.DrawBoards(theBoard)
                print("Oyunu Kazandınız!!!")
                gameIsPlaying = False
            else:

                if CreatBoard.isBoardFull(theBoard):
                    CreatBoard.DrawBoards(theBoard)
                    print("Oyun Berabere")
                    break
                else:
                    if CreatBoard.isBoardFull(theBoard):
                        CreatBoard.DrawBoards(theBoard)
                    else:
                        turn ="computer"
        else:
            move = CreatMove.getComputerMove(theBoard,computerLetter) 
            CreatMove.makeMove(theBoard,move,computerLetter)
            if CreatMove.isWinner(theBoard,computerLetter): 
                CreatBoard.DrawBoards(theBoard)
                print("Bilgisayar Kazandı! Oyunu Kaybettiniz")
            else:

                if CreatBoard.isBoardFull(theBoard):
                    CreatBoard.DrawBoards(theBoard)
                    print("Oyun Berabere")
                    break
                else:
                    turn = "player"
    
   if not CreatPlayer.playAgain():
         break

