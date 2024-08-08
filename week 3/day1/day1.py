#loops 
#2 methods of constructing loops
#loops are about tasks that need to repeat
#
#To understand the uses for a loop
#to understand the uses of a while loop
#to tell the difference between for and while loops
#to write programs using both for and while loops


# fav_drinks = ["tea", "juice","water"
#               ]
# # print(fav_drinks)

# print(fav_drinks[0])
# print(fav_drinks[1])
# print(fav_drinks[2])
# print(fav_drinks)

# better way 

# fav_drinks=[
#     "juice",
#     "tea",
#     "water"
# ]
# for i in fav_drinks:
#     print(i)

# parts = [
#     "wheels",
#     "tyres",
#     "windshield",
# ]
# for components in parts:
#     print(components)


#top 10 songs

# song =[
#     "Linkin Park  - One more light",
#     "Robbie Williams - Angels",
#     "Queen - Bohemian Rapsody",
#     "Eminem - Toy Soldiers",
#     "Eminem - Houdini",
#     "Linkin Park -  In the end ",
#     "Jay-z and Linkin Park - Numb",
#     "50 cent - In the Club",
#     "Katy Perry - Fireworks",
#     "Adele - Hometown Glory"
# ]
# for bestsong in song :
#     print (f"I love this song  * {bestsong}" )


#for loops:
#iterate through a sequence , execute a block of code as many things as there in the sequence , run a finite amount of times , they will always eventually stop

#do we need a list in order to construct a for loop ?

#Ranges

#generates a sequence for us to iterate throught

# for i in range(10):
#        print(i)

#range needs 1 argument - but is actually using 3.

# for i in range(10):
#     print(i)

# for i in range(0,10,3): - it means the steps. not even or odd numbers
#     print(i) 

    # example of step ^

#range only needs us to define the stop value.

#by default, we will start at 0 and up by 1 each time
#example for i in range (0,10,1)
  #print(i)

# for i in range (5,11):
#     print(i)

# for i in range (2,12,2):
#     print(i)

# for i in range (0,100):
#     print(i)

  # ACTIVITIES


#task 1 

# for i in range (1,11):
#     print(i)

# #task 2

# for i in range (2,12,2):
#     print(i)


      # print(i)


#task 3

# for i in range (1,11)[::-1]:
#       print(i)

#While
#while loop will run infinitely until a certain condition is met
#to fix this will need to input the input again
#for example

# answer = input("Who ordered a cortado?" )

# while answer!=  "Alex":
#       print("incorect")
#       answer = input("Who ordered a cortado?" )
# else:
#       print("correct")


# count = 1
# while count < 10:
#   print(f"Count is : {count}")
# count += 1



  
    


