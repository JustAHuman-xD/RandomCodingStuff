import time
import os
from random import randint

def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

Play = input("Would you like to play Rock Paper Scissors? (y/n) ")
Hands = [
  [
    ["",0],
    ["",0],
    ["    _______",2],
    ["---'   ____)",1],
    ["      (_____)",0],
    ["      (_____)",0],
    ["      (____)",1],
    ["---.__(___)",2],
  ],
  [
    ["",0],
    ["",0],
    ["    _______",2],
    ["---'   ____)",1],
    ["      (_____)",0],
    ["      (_____)",0],
    ["      (____)",1],
    ["---.__(___)",2],
  ],
  [
    ["",0],
    ["",0],
    ["    _______",7],
    ["---'    ____)____",1],
    ["           ______)",0],
    ["          _______)",0],
    ["         _______)",1],
    ["---.__________)",3],
  ],
  [
    ["",0],
    ["",0],
    ["    _______",7],
    ["---'    ____)____",1],
    ["           ______)",0],
    ["          _______)",0],
    ["         _______)",1],
    ["---.__________)",3],
  ],
  [
    ["",0],
    ["",0],
    ["    _______",7],
    ["---'   ____)____",2],
    ["          ______)",1],
    ["       __________)",0],
    ["      (____)",6],
    ["---.__(___)",7],
  ],
  [
    ["",0],
    ["",0],
    ["    _______",7],
    ["---'   ____)____",2],
    ["          ______)",1],
    ["       __________)",0],
    ["      (____)",6],
    ["---.__(___)",7],
  ],
  [
    ["    _______",],
    ["---'   ____)",],
    ["      (_____)",],
    ["      (_____)",],
    ["      (____)",],
    ["---.__(___)",],
    ["",],
    [""]
  ]
]

AIHands = [
  [
    ["",0],
    ["",0],
    ["_______    ",2],
    ["(____   '---",1],
    ["(_____)      ",0],
    ["(_____)      ",0],
    ["(____)      ",1],
    ["(___)__.---",2],
  ],
  [
    ["",0],
    ["",0],
    ["_______     ",6],
    ["____(____    '---",1],
    ["(______           ",0],
    ["(_______          ",0],
    ["(_______         ",0],
    ["(__________.--- ",2]
  ],
  [
    ["",0],
    ["",0],
    ["_______    ",7],
    ["____(____   '---",2],
    ["(______          ",1],
    ["(__________       ",0],
    ["(____)      ",6],
    ["(___)__.---",7]
  ],
]

Index = ["ROCK","R","PAPER","P","SCISSORS","S","UP"]
AIIndex = ["Rock","Paper","Scissors"]


def RPS():

  screen_clear()

  global Selection
  Selection = "Nothing"

  def Hand(Hand):
    for string in Hands[Hand]:
      print(string[0])

  def Shoot(Choice):
    screen_clear()
    AINumber = randint(0,2)
    AIHand = AIHands[AINumber]
    AIChoice = AIIndex[AINumber]
    PlayerNumber = Index.index(Choice.upper())
    PlayerHand = Hands[PlayerNumber]
    for i, string in enumerate(PlayerHand):
      toprint = string[0].ljust(len(string[0])+string[1]+AIHand[i][1])
      print(toprint+"      "+AIHand[i][0])
      if not (Choice.lower()).capitalize() in AIIndex:
        Choice = Index[PlayerNumber-1]
    print((Choice.lower()).capitalize()+"  VS  "+AIChoice)
    PlayerNumber = AIIndex.index((Choice.lower()).capitalize())
    if (AINumber + 1 == PlayerNumber or AINumber -2 == PlayerNumber):
      time.sleep(1)
      print("You Won!")
      time.sleep(1)
      print("Congradulations!")
      time.sleep(1)
      Again = input("Would you like to play Again? (y/n) ")
      if (Again.upper() == "YES" or Again.upper() == "Y"):
        RPS()
    elif (PlayerNumber + 1 == AINumber or PlayerNumber -2 == AINumber):
      time.sleep(1)
      print("You Lost!")
      time.sleep(1)
      print("Better Luck Next Time!")
      time.sleep(1)
      Again = input("Would you like to play Again? (y/n) ")
      if (Again.upper() == "YES" or Again.upper() == "Y"):
        RPS()
    else:
      time.sleep(1)
      print("Its a Tie!")
      time.sleep(1)
      print("Unlucky, maybe next game!")
      time.sleep(1)
      Again = input("Would you like to play Again? (y/n) ")
      if (Again.upper() == "YES" or Again.upper() == "Y"):
        RPS()

  def Choose():
    global Selection
    screen_clear()
    Hand(0)
    time.sleep(0.3)
    Selection = input("Rock(R), Paper(P), or Scissors(S)? ")
    if not Selection.upper() in Index:
      responses = ["Nice Try","Give me an actual answer","Seriously stop wasting time","You are annoying you know that...","Is This Edie?","C'monnnnn just answer","Lets just get this over with","You know i'm gonna win lets just do this."]
      print(responses[randint(0,4)])
      time.sleep(1)
      Choose()

  Choose()
  time.sleep(randint(1,2)*(1+(randint(1,5)/10)))
  print("Alright, Im Ready")
  time.sleep(1)
  screen_clear()
  Hand(6)
  print("Rock!")
  time.sleep(.3)
  screen_clear()
  Hand(0)
  print("Rock!")
  time.sleep(.3)
  screen_clear()
  Hand(6)
  print("Paper!")
  time.sleep(.3)
  screen_clear()
  Hand(0)
  print("Paper!")
  time.sleep(.3)
  screen_clear()
  Hand(6)
  print("Scissors!")
  time.sleep(.3)
  screen_clear()
  Hand(0)
  print("Scissors!")
  time.sleep(.3)
  screen_clear()
  Hand(6)
  print("Shoot!!")
  time.sleep(.3)
  screen_clear()
  Hand(0)
  print("Shoot!!")
  Shoot(Selection)
    
if (Play.upper() == "Y" or Play.upper() == "YES"):
  RPS()
else:
  print("Alright, I see how it is...")
  time.sleep(.3)
  screen_clear()
  print(".")
  time.sleep(.3)
  screen_clear()
  print("..")
  time.sleep(.3)
  screen_clear()
  print("...")
  time.sleep(.3)
  screen_clear()
  print(".")
  time.sleep(.3)
  screen_clear()
  print("..")
  time.sleep(.3)
  screen_clear()
  print("...")
  time.sleep(1)
  screen_clear()
  print("You're just afraid you will lose >:)")