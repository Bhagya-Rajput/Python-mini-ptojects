class Game():
   def __init__(self):
     self.lst =[0,1,2,3,4,5,6,7,8]
     self.player = "X"
     self.combinations = [ (0,3,6) , (1,4,7) , (2,5,8) , (0,1,2) , (3,4,5) , (6,7,8) , (0,4,8) , (2,4,6) ]
     self.lst2 = []
   def boards(self):
      for i in range(3):
         for j,k in zip(range(3),self.lst[i*3:(i+1)*3]):
            print((f" {k+1} " if isinstance(k,int) else f" {k} ") ,end = "|"if j<2  else '\n')
         print("----------" if i<2 else "")

   def Input(self):

      try:
         position = int(input("enter the desire position for X :"))
         if(1<= position<=9):
            index = position - 1
            if (self.lst[index] != "X" and self.lst[index] != "O"):
             self.lst[index]="X" if self.player == "X" else self.lst[index]="O"
            else:
             print("You enterd wrong position ")
         else :
            print("Enter the position from board")
      except ValueError as e:
         print("you Enterd some wrong input",e)
   def check_winner(self):
         for i in self.combinations :
            a,b,c = i
            if self.lst[a] == self.lst[b] == self.lst[c] and self.lst[a] in( "X" or "O") :
                  print(f"{self.lst[a]} Wins!!!!!!!")
                  return True
         return False
  