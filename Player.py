import random
class Player():
    def __init__(self,letter) :
        self.letter = letter
        letter=" "
       
        
    def whoGoesFirst(self):
         if random.randint(0, 1) == 0:
              return 'player'
         else:
              return 'computer'

    def inputPlayerLetter(self):
        while not (self.letter == 'X' or  self.letter == "O"):
            print("X veya O dan birini seçiniz?")
            self.letter = input()
            return self.letter
            
    def playAgain(self):
        print('Tekrar oynamak istermisiniz? (evet veya hayır)')
        return input().lower().startswith('e')
    
    def X_or_O(self,letter):
        if letter == "X":
              computerLetter = "O"
        elif letter == "O":
             computerLetter = "X"
        return computerLetter
