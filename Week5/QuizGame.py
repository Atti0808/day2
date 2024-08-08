from random import choice

def askquestion(number, score):
    while True:
        validinputs=["A","B","C","D"]
        if number==1:
            correct="C"
            print("""Sample question. Correct is C.
                A. Sample Answer 1
                B. Sample Answer 2
                C. Sample Answer 3
                D. Sample Answer 4""")
            answer=input("Select an answer A B C or D:").upper()
            if answer not in validinputs:
                print("Error, please enter only A, B, C or D")
            elif answer==correct:
                print("Correct")
                score+=5
                break
            else:
                print(f"Incorrect, correct is {correct}")
                if score<=1:
                    score=0
                else:
                    score-=2
                break
            if number==2:
                correct="A"
                print("""Sample question. Correct is A.
                A. Sample Answer 1
                B. Sample Answer 2
                C. Sample Answer 3
                D. Sample Answer 4""")
                answer=input("Select an answer A B C or D:").upper()
                if answer not in validinputs:
                    print("Error, please type only A, B, C or D")
                elif answer==correct:
                    print("Correct")
                    score+=5
                    break
                else:
                 print("Incorrect")
                break
    return score


def playquiz():
    questions=[1,2,3,4,5]
    score=0
    while questions:
        number=choice(questions)
        score+=askquestion(number, score)
        print(f"Score is now {score}")
        questions.remove(number)
    print(f"{score}")

playquiz()
