#Magic Ball Program
from colorama import Back, Fore , Style 



import random

# answers1 = (" Yeap",
#            "Ofcourse",
#             "Ofcourse you will",
#             "I know you are " , 
#             "Guranteed"
# )            
# answer2 = ("Nope",
#            "Not going to happen",
#            "I can tell you from now it`s a no!",
#            "Why even bother"
           
#            )
num  = input("Please enter your Question : ")

print(random.randint(1,15))
# divided_by_2 = True
if num%2==0:
    print(Fore.GREEN + "Good Fortune")
else:
    print(Fore.RED + "Bad Fortune") 

# print(Style.RESET_ALL)

