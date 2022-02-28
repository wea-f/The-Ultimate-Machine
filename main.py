#Imports
import time
import random
from time import sleep
import os
from getkey import getkey, key
#colors
colorList = ["\033[0;31m", "\033[0;32m", "\033[0;33m", "\033[0;34m", "\033[0;35m", "\033[0;36m", "\033[0;37m", "\033[0;90m", "\033[0;91m", "\033[0;92m", "\033[0;93m", "\033[0;94m", "\033[0;95m", "\033[0;96m", "\033[0;97m"]#black(0), red(1), green(2), yellow(3), blue(4) magenta(5), cyan(6),white(7), bright black(8), bright red(9), bright green(10) bright yellow(11), bright blue(12), bright magenta(13), bright cyan(14), bright white(15)
#"\033[0;30m" <-- black
#FUNCTIONS 
#function for timer 
def times(t):
 color = random.choice(colorList)
 start = time.time()
 end = time.time()
 while end - start < t:
   end = time.time()
   print(str(round(t - (end - start), 1)) + " seconds") 
   os.system("clear")
 typewrite(color + "Your timer ended!",0.07)
 checkReturnOption()

#function for RNG
def randNumVal():
  color = random.choice(colorList)
  colortwo = random.choice(colorList)
  colorthree = random.choice(colorList)
  typewrite("\nAnswer the questions. Then press enter. ",0.06)
  firstNum = float(input(colortwo + "\nWhat is minimum? (Number form please.) "))
  secNum = float(input(color +"What is the maximum? (Number form please.) "))
  gen_Num = str(round(random.uniform(firstNum, secNum),0))
  print(colorthree + "Your random number is: " + gen_Num)
  checkReturnOption()

#functions for add,subtract,multi,divide.
def add(a,b):
  col = random.choice(colorList)
  answer = str(a + b)
  print(col + "Your answer is: " + answer)
  checkReturnOption()

def sub(a,b):
  col = random.choice(colorList)
  answer = str(a - b)
  print(col + "Your answer is: " + answer)
  checkReturnOption()

def multi(a,b):
  col = random.choice(colorList)
  answer = str(a*b)
  print(col + "Your answer is: " + answer)
  checkReturnOption()
def divide(a,b):
  col = random.choice(colorList)
  answer = str(a/b)
  print(col + "Your answer is: " + answer)
  checkReturnOption()
#function for calculator
def calculate():
  colr = random.choice(colorList)
  colr2 = random.choice(colorList)
  colr3 = random.choice(colorList)
  typewrite("\nType in your answer, and press enter. ", 0.05)
  first = int(input(colr + "\nWhat is your first number? (1234 form please.) "))
  second = int(input(colr2 + "What is your second number? (1234 form please.) "))
  express = int(input( colr3 + "(1) add, (2) subtract, (3) multiply, (4) divide.) "))
  #Calculate by calling functions
  if express == 1:
    add(first, second)
  if express == 2:
    sub(first, second)
  if express == 3:
    multi(first, second)
  if express == 4:
    divide(first, second)
#Function for Coin Flip
def coinFlip():
  print("\n(1)Heads or (2)tails? ")
  num_key = getkey()
  flip = random.randint(1,2)
  #if the coin flip is a heads
  if flip == 1:
    green = colorList[9]
    red  = colorList[0]
    #if coin flip is heads and you choose heads:
    if num_key == "1":
      typewrite("Your coin flipped heads!! ", 0.055)
      typewrite(green + "\nYou have predicted correct!", 0.055)
      checkReturnOption()
      #if coin flip is heads but you chose tails:
    if num_key == "2":
      red  = colorList[0]
      typewrite("Your coin flipped tails!!", 0.055)
      typewrite(red + "\nYou have gotten it wrong. :( ", 0.055)
      checkReturnOption()
  elif flip == 2:
    #if coin flip is tails but you choose heads:
    red = colorList[0]
    if num_key == "1":
     typewrite("Your coin flipped heads!!",0.055)
     typewrite(red + "\nYou have gotten it wrong. :( ",0.055)
     checkReturnOption()
     #if coin flip is tails and you got it correct:
    if num_key == "2":
     green = colorList[9]
     typewrite("Your coin flipped tails! ",0.055)
     typewrite(green + "\nYou have predicted correct!",0.055)
     checkReturnOption()
#Stopwatch
def stopwatch():
  randColor = random.choice(colorList)
  typewrite("\nPress (h) to start the stopwatch. To end it, press (h). ", 0.01)
  let_key = getkey()
  if let_key == "t" or "T":
    typewrite("\nBegan stopwatch. ",0.015)
    beginTime = time.time()
    let_key = getkey()
    if let_key == "h" or "H":
     afterTime = time.time()
     totalTime = str(round(afterTime - beginTime,4))
     print(randColor + "\nYour total time was: " + totalTime + " seconds")
     checkReturnOption()
#Timer
def timer():
  randomColor2 = random.choice(colorList)
  typewrite("\nAnswer the questions, then press enter. \n", 0.05)
  timerLong = int(input("How long is your timer in seconds? If it's in minutes, press 0 then enter. "))
  if timerLong == 0:
   minutes = int(input(randomColor2 + "How long is your timer in minutes? "))
   sec = minutes * 60
   int(sec)
   times(sec)
  else:
    times(timerLong)
#Dice Roll function  
def diceRoll():
  sides = int(input("\nHow many sides is your die? (Min 4, Max, 20) "))
  if sides < 4:
    typewrite("Error, your number is lower than 4. Please try again.", 0.06)
  if sides > 20:
    typewrite("Error, your number is higher than 20.", 0.06)
  else:
    showDieRoll(sides)
#function for typewrite effect
def typewrite(message, delay):
 for i in str(message):
  print(i, end= "", flush = True)
  sleep(delay)

#function for printing and generating die roll
def showDieRoll(a):
  randomColor = random.choice(colorList)
  int(a)
  final_DR = random.randint(1, a)
  print(randomColor + "Your die rolled the number: " + str(final_DR))
  checkReturnOption()
#function for returning back to option "page"
def options():
  print("\n(1)Calculator, (2)RNG, (3)Coin Flip, (4)Stopwatch, (5)Timer, (6)Dice Roll, (7)Random option.  ")
  a = getkey()
  if a == "1":
    calculate()
  if a == "2":
    randNumVal()
  if a == "3":
    coinFlip()
  if a == "4":
    stopwatch()
  if a == "5":
    timer()
  if a == "6":
    diceRoll()
#check if option == random
  if a == "7":
    #generates random
    choice = random.randint(1,6)
    int(choice)
    if choice == 1:
      typewrite(colorList[9] + "Your random option was a calculator! ", 0.03)
      calculate()
    if choice == 2:
      typewrite(colorList[9] + "Your random option was a random number generator! ", 0.03)
      randNumVal()
    if choice == 3:
      typewrite(colorList[9] + "Your random option was a coin flip! ", 0.03)
      coinFlip()
    if choice == 4:
      typewrite(colorList[9] + "Your random option was a stopwatch! ", 0.03)
      stopwatch()
    if choice == 5:
      typewrite(colorList[9] + "Your random option was a timer! ", 0.03)
      timer()
    if choice == 6:
      typewrite(colorList[9] + "Your random option was a die roll! ", 0.03)
      diceRoll()


def checkReturnOption():
  randomcolor = random.choice(colorList)
  time.sleep(0.25)
  typewrite(randomcolor + "\nWould you like to go back to the options? (y for yes and n for no)",0.035)
  check = getkey()
  if check == "y":
    options()
  else:
    typewrite(colorList[0] + "\nWelp, goodbye. And thanks for 'playing' my project! ", 0.055)
    time.sleep(0.5)
    quit()

#Beggining of Script (All above were functions)
typewrite("Welcome to the The Greatest Supreme Ultimate Super Deluxe Machine++!! Directions are below. ", 0.045)
typewrite("\nPress the numbers associated with your choice.", 0.035)
#Calls option function
options()
