import time
import os
from random import randint

play = input("Would you like to play a game of Hangman? (y/n) ") #Hi

def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

def hangman():
  Words = [["Bell","Toy","Corn","Age","Bake","Ball","Band","Bee","Beef","Beep","Bird","Bike","Best","Call","Car","Cat","Cook","Crow","Cow","Cry","Cube","Damp","Deep","Deer","Dad","Date","Dent","Die","Dog","Doll","Eat","Fake"],["Hangman","Rolled","Fingers","Except","Speed","Catch","Itself","Mark","Button","Bargain","Certain","Orphan","Fountain","Oxen","Latitude","Compass","Absolute","Equator","Yourself","Maybe","Problem","Complete","Rather","Crowd","Fresh","Children"],["Abruptly","Foxglove","Lengths","Subway","Lucky","Frazzled","Abyss","Thumbscrew","Topaz","Nowadays","Vaporize","Unworthy","Oxidise","Glowworm","Grogginess","Marquis","Matrix","Mystify","Gossip","Haphazard","Bookworm","Blizzard","Axiom","Pajama","Transplant","Numbskull","Quizzes","Wheezy","Witchcraft","Cockiness","Jackpot","Phlehm","Pneumonia","Jaundice","Jawbreaker","Strength","Kilobyte","Fluffiness","Zigzag","Zombie","Xylophone","Sphinx","Kazoo"]]
  StickMen = [ #Frames For Hangman
    [
      "    ________  ",
      "    |       | ",
      "            | ",
      "            | ",
      "            | ",
      "            | ",
      "            | ",
      "          _____",
      ""
    ],
    [
      "    ________  ",
      "    |       | ",
      "   [ ]      | ",
      "            | ",
      "            | ",
      "            | ",
      "            | ",
      "          _____",
      ""
    ],
    [
      "    ________  ",
      "    |       | ",
      "   [ ]      | ",
      "    |       | ",
      "    |       | ",
      "            | ",
      "            | ",
     "          _____",
      ""
    ],
    [
      "    ________  ",
      "    |       | ",
      "   [ ]      | ",
      "    |       | ",
      "    |       | ",
      "   /        | ",
      "            | ",
     "          _____",
      ""
    ],
    [
      "    ________  ",
      "    |       | ",
      "   [ ]      | ",
      "    |       | ",
      "    |       | ",
      "   / \      | ",
      "            | ",
      "          _____",
      ""
    ],
    [
      "    ________  ",
      "    |       | ",
      "   [ ]      | ",
      "    | \     | ",
      "    |       | ",
      "   / \      | ",
      "            | ",
      "          _____",
      ""
    ],
    [
      "    ________  ",
      "    |       | ",
      "   [ ]      | ",
      "  / | \     | ",
      "    |       | ",
      "   / \      | ",
      "            | ",
      "          _____",
      ""
    ],
    [
      "    ________  ",
      "    |       | ",
      "   [><]     | ", #[º.º]
      "  / | \     | ", #[Uwu]
      "    |       | ",
      "   / \      | ",
      "            | ",
      "          _____",
      ""
    ]
  ]
  global Mistakes
  global MistakesString
  Mistakes = 0
  MistakesString = "Incorrect Letters: "
  Word = "Blank"
  Difficultys = [["Easy",0],["Medium",1],["Hard",2]]
  Guessable = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
  AlreadyGuessed = [[],[]]
  Guess = []
  Ended = "false"
  
  def SelectWord(diffnum):
    print(Difficultys[diffnum][0]+" Selected!")
    time.sleep(0.5)
    return Words[diffnum][randint(0, len(Words[diffnum])-1)]

  def Mistake(Letter):
    global Mistakes
    global MistakesString
    Mistakes = Mistakes + 1
    MistakesString = MistakesString+Letter.upper()+" "
    return [Mistakes,MistakesString]

  def Correct(Letter):
    for i, character in enumerate(Word):
        if (character.upper() == Letter.upper()):
          Guess[i] = Letter.upper()+" "

  def Move():
    screen_clear()

    for string in StickMen[Mistakes]:
      print(string)
    
    printGuess = ""

    for string in Guess:
      printGuess = printGuess+string
    print("Mistakes: "+str(Mistakes))
    print(MistakesString)
    print(printGuess)
    print("")

    Letter = input("What is Your Guess? Letter: ")
    if Letter.upper() not in AlreadyGuessed[0] and Letter.upper() not in AlreadyGuessed[1] and Letter.upper() in Guessable:
      AlreadyGuessed[0].insert(0,Letter.upper())
      if Letter.upper() in Word.upper():
        print("Your Letter is Correct!")
        time.sleep(0.5)
        print(str(len(Word)-len(AlreadyGuessed[0]))+" Letters Remaining!")          
        Correct(Letter)
      else:
        AlreadyGuessed[1].insert(0,Letter.upper())
        print("Your Letter is not Correct! Dun Dun Dun....")
        time.sleep(1)
        Mistake(Letter)
    elif Letter.upper() not in Guessable:
      print("That is not a Letter, try again!")
      time.sleep(1)
    else:
      print("You already Guessed That, try again!")
      time.sleep(1)

  print("What Difficulty Would you Like?")
  time.sleep(0.5)
  print("Easy, Medium, or Hard? Type your Answer! ")
  Difficulty = input("Any other Input will Result in a Random Difficulty. Difficulty: ")
  time.sleep(0.5)
 
  
  for list in Difficultys:
      if (list[0].upper() == Difficulty.upper() or list[0][:1].upper() == Difficulty.upper()):
        Word = SelectWord(list[1])

  if (Word == "Blank"):
    diffnum = randint(0,2)
    Difficulty = Difficultys[diffnum][0]
    Difficulty = Difficulty.upper()
    Word = SelectWord(diffnum)
  
  for character in Word:
      Guess.insert(0,"_ ")
  
  while (Ended == "false"):
    Move()
    if (Mistakes == 7):
      screen_clear()

      for string in StickMen[Mistakes]:
        print(string)
    
      printGuess = ""

      for string in Guess:
        printGuess = printGuess+string
      print("Mistakes: "+str(Mistakes))
      print(MistakesString)
      print(printGuess)
      print("")
      print("Your Word Was: "+Word)
      time.sleep(1)
      print("You Have Lost!")
      Ended = "True"
      time.sleep(1)
      Again = input("Would you like to play again? (y/n) ")
      if (Again.upper() == "Y" or Again.upper() == "YES"):
        hangman()
    else:
      global found
      found = 0
      for string in Guess:
        if string.find("_"):
          found +=1
      if (found == len(Word)):
        Ended = "True"
        screen_clear()

        for string in StickMen[Mistakes]:
          print(string)
    
        printGuess = ""

        for string in Guess:
          printGuess = printGuess+string
        print("Mistakes: "+str(Mistakes))
        print(MistakesString)
        print(printGuess)
        print("")
        print("You have Won!")
        time.sleep(1)
        Again = input("Would you like to play again? (y/n) ")
        if (Again.upper() == "Y" or Again.upper() == "YES"):
          hangman()
      

  
  

if (play.upper() == "Y" or play.upper() == "YES"):
  hangman()
else:
  print("Oh... Okay")
  time.sleep(1)
  print("Bye I Guess")