from random import choice
import colorama
from colorama import Fore

record=[]
#record if defined outside of the function so that it
#doesn`t reset when the function is called
# 
# 
# askquestion is defined here to prevent redundany in the playquiz function
# `
def askquestion(questionnumber ,questionorder):
 
 

    score = 0
    
    #validinputs prevents the player from entering anything else than A, B, C or D 
    validinputs=["A","B","C","D"]
    #the while loop ensure the question will repeat  if an invalid input is entered
    while True:
        print(f"question{questionorder}")
    #each question has it`s own number to ensure only one is asked at a time `    
        if questionnumber==1:
        #the correct answer is defined within the if statement so that will always be re-defined when a different question is asked
            correct="B"
            correcttext="[]"  
            print("""
         Which type of brackets are used for list?.
                  
                A. Curly Brackets {}
                B. Square Brackets []
                C. Paranthases ()
                D. Angle Brackets <>
                """)
            
        elif questionnumber==2:
            correct="C"
            correcttext="True or False"
            print("""
                  
         What data type is a Boolean?.
                  
                A. Whole Number
                B.Text
                C. True or False
                D. Decimal number 4
                """)  
                  
        elif questionnumber==3:
            correct="D"
            correcttext="all of the above"
            print("""
                  
        How do you end a while loop?.
                A. break
                B. return
                C. the condition is no longer True
                D. all of the above
                """)
            
        elif questionnumber==4:
            correct="B"
            correcttext="num%2==0"
            print("""
                  
         Wich of the following will check if the value is even?.
                  
                A. num/2==True
                B. num%2==0
                C. num%num==0
                D. num=even==True
                """)
            
        elif questionnumber==5:
            correct="C"
            correcttext="from library import function"
            print("""
        How do you add a specific function from a library?.
                  
                A. from library import function
                B. import library
                C. from library import function
                D. import function
                """)
            
        else:
            "Error: Invalid question number was generated"
            return 0
        answer=input("Select an answer A B C or D:").upper()
        if answer not in validinputs:
            print("Error, please enter only A, B, C or D")
        elif answer==correct:
            print(Fore.GREEN+f"Correct, the answer is {correcttext}"+Fore.RESET)
            return 5
        else:
            print(Fore.RED+f"Incorrect, correct is {correcttext}"+Fore.RESET)
            return -2

def playquiz():
    print("Welcome to the Python Programing Game")
    #this list defines the range the random choice can pull from , it would need to be manually updated if more questions are added
    questions=[1,2,3,4,5]
    #score is initialised so that is resets between rounds
    score=0
    questionorder =1
    #this while loop will continue until questions has no data left
    while questions:
        #random options from questions (5 , -2 or 0 if error ) is then added to score
        number=choice(questions)
        score+=askquestion(number , questionorder)
        #if the restult in score is a negative it resets to 0 
       
        if score<0:
            score=0
        print(f"Score is now {score}")
        questionorder+=1
        #the question number that was chose at random is moved from the list so that it cannot be chosen again
        # #this eventually results in the list being empty so that the while loop ends. 
        questions.remove(number)
        #final result printed
    print(f"Your final score is {score}!")
    if record:
        if all(score>x for x in record):
        #this if statement checks if the player has already played a round and if so , displays their previous scores.    
            print("New high score!")
        print(f"Your previous scores were: {record}")
        #thhe currenct score is save to the record list
    record.append(score)
    #this while loop repeateadly asks if the player want to play again until it`s selects No 
    #if yes, the game restarts , with the previous score saved. the break after playquiz()ensures that the game ends when the player says no 
    while True:
        playagain=input("Play again? Y for Yes N for No  ").upper()
        if playagain=="Y":
            playquiz()
            break
        elif playagain=="N":
            print("Thanks for playing!")
            break
        else:
            print("Error, please input Y or N")


playquiz()

