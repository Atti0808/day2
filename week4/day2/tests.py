import random                        #imports a random moduel for the computer.
game = ["ROCK", "PAPER", "SCISSORS"]  #sets the game answers.
count = 0                             #game count is set to zero.
score = 0                             #player score is set to zero.
computerscore =0                      #computers score is set to zero.

print ("Welcome")
while count == 0:                     #starts game if count is zero.
  for i in range (7):                  #repeats the turns 3 times.
    answer = input ("Pick rock, paper or scissors.")     #users answer.

    print (answer.upper())                               # prints the users answer
    computer= random.choice(game)                        #computer picks randomly

    print ("Computer picks",computer)                    #prints the computers choice.

    if answer.upper() == "ROCK" and computer == "ROCK":          #This whole set of code sets the game that what beats what.
      print ("Its a tie!")                                       # prints after each response that who won.
      count +=1                                                  #the count variable is increased.

    elif answer.upper() == "PAPER" and computer == "PAPER":
      print ("Its a tie!")
      count +=1

    elif answer.upper() == "SCISSORS" and computer == "SCISSORS":
      print ("Its a tie!")
      count +=1

    elif answer.upper() == "PAPER" and computer == "ROCK":
      print ("You win!")
      count +=1
      score +=1                                                 #user score is added.

    elif answer.upper() == "PAPER" and computer == "SCISSORS":
      print ("You lose!")
      count +=1
      computerscore +=1                                         #computers score is added.

    elif answer.upper() == "ROCK" and computer == "PAPER":
      print ("You lose!")
      count +=1
      computerscore +=1

    elif answer.upper() == "ROCK" and computer == "SCISSORS":
      print ("You win!")
      count +=1
      score +=1

    elif answer.upper() == "SCISSORS" and computer == "ROCK":
      print ("lose!")
      count +=1
      computerscore +=1

    elif answer.upper() == "SCISSORS" and computer == "PAPER":
      print ("You win!")
      count +=1
      score +=1


if score < computerscore:                      #prints out at the end who scored how much and who won.
  print ("Your score is", score)
  print ("Computers socre is",computerscore)
  print ("Computer wins!.")

if score > computerscore:
  print ("Your score is", score)
  print ("Computers socre is",computerscore)
  print ("You win!.")

if score == computerscore:
  print ("Your score is", score)
  print ("Computers socre is",computerscore)
  print ("Its a tie!!.")
