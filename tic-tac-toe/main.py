class Game():
   def __init__(self):
     self.lst =[0,1,2,3,4,5,6,7,8]
     self.player = "X"
     self.combinations = [ (0,3,6) , (1,4,7) , (2,5,8) , (0,1,2) , (3,4,5) , (6,7,8) , (0,4,8) , (2,4,6) ]
     self.result = None
   def boards(self):
      for i in range(3):
         for j,k in zip(range(3),self.lst[i*3:(i+1)*3]):
            print((f" {k+1} " if isinstance(k,int) else f" {k} ") ,end = "|"if j<2  else '\n')
         print("----------" if i<2 else "")

   def Input(self):

      try:
         position = int(input(f"enter the desire position for {self.player} :"))
         if(1<= position<=9):
            index = position - 1
            if self.lst[index] not in ("X", "O"):
             self.lst[index]= self.player  
             return True
            else:
             print("You enterd wrong position ")
             return False
         else:
            print("Enter the position from the")
            return False
      except ValueError as e:
         print("you Enterd some wrong input",e)
         return False
   def check_winner(self):
         for i in self.combinations :
            a,b,c = i
            if self.lst[a] == self.lst[b] == self.lst[c] and self.lst[a] in ("X", "O") :
                  print(f"{self.lst[a]} Wins!!!!!!!")
                  return True
         return False
   def draw(self):
         for item in self.lst:
            if isinstance(item,int):
               return False
         return True
       
        
         
game = Game()
while True:
      while True:
         game.boards()
         while True:
          valid_position = game.Input()
          if valid_position:
            break
          else:
            continue
         game.result = game.check_winner()
         if game.result:
            break
         else:
            result2 = game.draw()
            if result2 == False:
              game.player = "O" if game.player == "X" else "X"
            else:
              print("THE Game is Drawn")
              break
      game.boards()
      n = input("enter if you want to play game again{y/n}").lower().strip()
      if(n=="y"):
         game = Game()
         continue
      else:
         break