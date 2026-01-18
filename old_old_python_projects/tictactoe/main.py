import os
import time

numbers = [1,2,3,4,5,6,7,8,9]
symbols = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
filled = []

def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

def tutorial():
  board = [
    "       |      |      ",
    "   1   |  2   |  3   ",
    " ______|______|______",
    "       |      |      ",
    "   4   |  5   |  6   ",
    " ______|______|______",
    "       |      |      ",
    "   7   |  8   |  9   ",
    "       |      |      "
  ]
  print("Welcome to Tic Tac Toe!")
  time.sleep(1)
  know = input("Do you know how to play? (y/n) ")
  if (know.upper() == "Y" or know.upper() == "YES"):
    print("Alright lets Play!")
    time.sleep(1)
    screen_clear()
    tictactoe()
  else:
    screen_clear()
    print("Okay let me tell you how to play!")
    time.sleep(1)
    screen_clear()
    for string in board:
      print (string)
    def Try():
      screen_clear()
      for string in board:
        print (string)
      print("On your turn you will type a Number corresponding to a number on the chart.")
      number = input("Go ahead and try that now!: ")
      if not int(number) in numbers:
        print("Whoops, looks like you didnt type the right number, its a number between 1 and nine")
        time.sleep(1)
        Try()
      else:
        screen_clear()
        for string in board:
          newstring = ""
          for i in string:
            if i == number:
              i = "X"
            newstring += i
          print(newstring)
          board[board.index(string)] = newstring
        print("Good Job! Look at the board and you can see your X")
        time.sleep(1)
        print("Thats basically all you need to know so go ahead and play!")
        input("Press Enter to continue...")
        time.sleep(1)
        screen_clear()
        tictactoe()
    Try()



def tictactoe():

  def PVP():
    board = [
      "       |      |      ",
      "   1   |  2   |  3   ",
      " ______|______|______",
      "       |      |      ",
      "   4   |  5   |  6   ",
      " ______|______|______",
      "       |      |      ",
      "   7   |  8   |  9   ",
      "       |      |      "
    ]
    referenceboard = [
     1,2,3,4,5,6,7,8,9
    ]
    NumberOfMoves = 0
    global Ended
    global P1S
    global P2S
    Ended = "false"
    print("Lets Meet our Players!")
    time.sleep(1)
    P1 = input("Player One's Name: ")
    P1S = ""
    time.sleep(1)
    P2 = input("Player Two's Name: ")
    P2S = ""
    time.sleep(1)
    
    def GetSymbols(): 
      global P1S
      global P2S
      screen_clear()
      print("Now you both get to pick your symbol!")
      time.sleep(0.5)
      print("Your symbol is what is drawn when you fill in a space.")
      time.sleep(0.5)
      print("Simply just type what you want your symbol to be, for example: X")
      time.sleep(0.5)
      print("The only thing you can set as your symbol is a letter.")
      time.sleep(0.5)
      print("So dont try anything else. Im looking at you Edie.")
      time.sleep(0.5)
      def Symb(player):
        global P1S
        global P2S
        symbol = input(player+" Type your Symbol now: ")
        if not symbol.upper() in symbols:
          print("I literally told you only letters are allowed....")
          time.sleep(1)
          print("Try again")
          time.sleep(1)
          screen_clear()
          Symb(player)
        else:
          if (player == P1):
            P1S = symbol
          else:
            P2S = symbol
      Symb(P1)
      Symb(P2)

    def UpdateBoard(number,PS):
      for string in board:
          newstring = ""
          for i in string:
            if i == number:
              i = PS.upper()
              filled.insert(0,number)
            newstring += i
          print(newstring)
          board[board.index(string)] = newstring

    def Try():
      global number
      number = 0
      def TryNum():
        global number
        number = input("Number: ")
        if not number.isdigit() or number.isdigit() and not int(number) in numbers:
          print("Whoops, looks like you didnt type the right number.")
          print("You need a number between 1 and 9")
          time.sleep(1)
          TryNum()
        if number.isdigit() and int(number) in numbers:
          testnumber = int(number)
          if testnumber/3 < 1:
            if not board[1][referenceboard[testnumber-1]] == number:
              print("Slot is Already Taken")
              time.sleep(0.5)
              print("Nice Try Cheater")
              TryNum()
      TryNum()
      return number

    def IndexBoard():
      def index(number):
        for string in board:
          if not (string.find(str(number)) == -1):
            referenceboard[number-1] = string.find(str(number))
      index(1)
      index(2)
      index(3)
      index(4)
      index(5)
      index(6)
      index(7)
      index(8)
      index(9)

    def Turn():
      global Ended
      screen_clear()
      for string in board:
        print(string)
      print("")
      print(P1+" It's your turn! Type a number from 1 - 9!")
      number = Try()
      screen_clear()
      UpdateBoard(number,P1S)
      Victor = CheckVictory()
      if not (Victor == "NoOne"):
        print(P1+" Has Won! Congradulations!")
        Ended = "true"
      elif len(filled) == 9:
        print("Its a Cat! Nobody wins!")
        Ended = "true"
      else:
        print("")
        print(P2+" It's your turn! Type a number from 1 - 9!")
        number = Try()
        screen_clear()
        UpdateBoard(number,P2S)
        Victor = CheckVictory()
        if not (Victor == "NoOne"):
          print(P2+" Has Won! Congratulations!")
          Ended = "true"
        elif len(filled) == 9:
          print("Its a Cat! Nobody wins!")
          Ended = "true"

    def CheckVictory():
      global Victor
      Victor = "NoOne"
      line1 = board[1]
      v1 = 3
      line2 = board[4]
      v2 = 10
      line3 = board[7]
      v3 = 17
      def Check(P, S):
        global Victor
        for line in board:
          if (line[v1] == S and line[v2] == S and line[v3] == S and Victor == "NoOne"):
            Victor = P
        if line1[v1] == S and line2[v2] == S and line3[v3] == S or line1[v3] == S and line2 [v2] == S and line3[v1] == S and Victor == "NoOne":
          Victor = P
        if (line1[v1] == S and line2[v1] == S and line3[v1] == S or line1[v2] == S and line2[v2] == S and line3[v2] == S or line1[v3] == S and line2[v3] == S and line3[v3] == S):
          Victor = P
      Check(P1,P1S.upper())
      Check(P2,P2S.upper())
      return Victor

    IndexBoard()
    GetSymbols()
    while Ended == "false":
      Turn()
      if not (Ended == "false"):
        Again = input("Do you wanna play again? (y/n) ")
        if (Again.upper() == "Y" or Again.upper() == "YES"):
          tutorial()

  PVP()

play = input("Would you like to play a game of Tic Tac Toe? (y/n) ")
if (play.upper() == "Y" or play.upper() == "YES"):
  tutorial()
else:
  print("You're boring")

