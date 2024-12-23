import random
board = [[1,2,3],[4,5,6],[7,8,9]]
#print(board)

#Prints board function
def print_board(board):
  print("-" * 9)
  for row in board:
        print(" | ".join(map(str, row)))
        print("-" * 9)
  #print_board(board)


#Dictionary containing indicces



def computer_turn(board):
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    if(board[x][y] == 'x' or board[x][y] == 'o'):
      computer_turn(board)
    else:
     print()
     print("Computer's Turn --------")
     board[x][y] = 'x'
     print_board(board)


#computer_turn(board)
def user_turn(board):
  print()
  x=0
  while(x<1):
   i = int(input("Enter a number to place 'o': "))
   if(i == 1):
    if(check_valid(board,1)):
     board[0][0] = 'o'
     print()
     x=x+1
     print_board(board)
   if(i == 2):
    if(check_valid(board,2)):
     print()
     board[0][1] = 'o'
     print()
     x=x+1
     print_board(board)
   if(i == 3):
    if(check_valid(board,3)):
     board[0][2] = 'o'
     print()
     x=x+1
     print_board(board)
   if(i == 4):
    if(check_valid(board,4)):
     board[1][0] = 'o'
     print()
     x=x+1
     print_board(board)
   if(i == 5):
    if(check_valid(board,5)):
     board[1][1] = 'o'
     print()
     x=x+1
     print_board(board)
   if(i == 6):
    if(check_valid(board,6)):
     board[1][2] = 'o'
     print()
     x=x+1
     print_board(board)
   if(i == 7):
    if(check_valid(board,7)):
     board[2][0] = 'o'
     print()
     x=x+1
     print_board(board)
   if(i == 8):
    if(check_valid(board,8)):
     board[2][1] = 'o'
     print()
     x=x+1
     print_board(board)
   if(i == 9):
    if(check_valid(board,9)):
     board[2][2] = 'o'
     print()
     x=x+1
     print_board(board)

def check_valid(board,place):
   if(place == 1):
     if(board[0][0] == 'x' or board[0][0] == 'o'):
      return False
     else:
      return True
   if(place == 2):
     if(board[0][1] == 'x' or board[0][1] == 'o'):
      return False
     else:
      return True
   if(place == 3):
     if(board[0][2] == 'x' or board[0][2] == 'o'):
      return False
     else:
      return True
   if(place == 4):
     if(board[1][0] == 'x' or board[1][0] == 'o'):
      return False
     else:
      return True
   if(place == 5):
     if(board[1][1] == 'x' or board[1][1] == 'o'):
      return False
     else:
      return True
   if(place == 6):
     if(board[1][2] == 'x' or board[1][2] == 'o'):
      return False
     else:
      return True
   if(place == 7):
     if(board[2][0] == 'x' or board[2][0] == 'o'):
      return False
     else:
      return True
   if(place == 8):
     if(board[2][1] == 'x' or board[2][1] == 'o'):
      return False
     else:
      return True
   if(place == 9):
     if(board[2][2] == 'x' or board[2][2] == 'o'):
      return False
     else:
      return True



dict = {
    1:board[0][0],
    2:board[0][1],
    3:board[0][2],
    4:board[1][0],
    5:board[1][1],
    6:board[1][2],
    7:board[2][0],
    8:board[2][1],
    9:board[2][2]
}


def win_game(board):
    #1st row
  if (board[0][0] == board[0][1] == board[0][2] == 'x' or board[0][0] == board[0][1] == board[0][2] == 'o'):
    return True
    #2nd row
  elif (board[1][0] == board[1][1] == board[1][2] == 'x' or board[1][0] == board[1][1] == board[1][2] == 'o'):
    return True
    #3rd row
  elif (board[2][0] == board[2][1] == board[2][2] == 'x' or board[2][0] == board[2][1] == board[2][2] == 'o'):
    return True
    #1st col
  elif (board[0][0] == board[1][0] == board[2][0] == 'x' or board[0][0] == board[1][0] == board[2][0] == 'o'):
    return True
    #2nd col
  elif (board[0][1] == board[1][1] == board[2][1] == 'x' or board[0][1] == board[1][1] == board[2][1] == 'o'):
    return True
    #3rd col
  elif (board[0][2] == board[1][2] == board[2][2] == 'x' or board[0][2] == board[1][2] == board[2][2] == 'o'):
    return True
    #1st diagonal
  elif (board[0][0] == board[1][1] == board[2][2] == 'x' or board[0][0] == board[1][1] == board[2][2] == 'o'):
    return True
    #2nd diagonal
  elif (board[0][2] == board[1][1] == board[2][0] == 'x' or board[0][2] == board[1][1] == board[2][0] == 'o'):
    return True
  else:
    return False
  





def run(board):
  flg = 2
  while(flg<=9):
    computer_turn(board)
    if(win_game(board)):
      print()
      print("COMPUTER WON")
      break
    user_turn(board)
    if(win_game(board)):
      print()
      print("YOU WON")
      break
    flg+=2
   #print(flg)
  if(not(win_game(board))):
    computer_turn(board)
    if(win_game(board)):
      print()
      print("COMPUTER WON")
  print()
  print("GAME OVER")

run(board)
