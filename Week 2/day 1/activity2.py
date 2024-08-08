num = int(input("please input a number: "))
divided_by_3 = False
if((num % 3 ) == 0):
       divided_by_3 = True

divided_by_5 = False
if((num % 5) == 0) :
    divided_by_5 = True

    if(divided_by_3 and divided_by_5):
          print("The number %d is divided by 3 and 5." %num)
elif(divided_by_3):
      print("The number %d is divided by 3 ." %num)   
elif(divided_by_5):
      print("The number is divided by 5."% num)
else:
      print("The number %d is not divded neither by 3 or 5 " % num)                  


#correct way 

# number = 9


# if number%3==0 or number%5==0 and num != 0:
#       print("This number is divisible by 3 or 5")
# else:
#       print("this number is not divisible by 3 or 5 ")      