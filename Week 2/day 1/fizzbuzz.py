num = int(input("please input a number: "))
divided_by_3 = False
if((num % 3 ) == 0):
       divided_by_3 = True

divided_by_7 = False
if((num % 7) == 0) :
    divided_by_7 = True

    if(divided_by_3 and divided_by_7):
          print("%d fizzbuzz." )
elif(divided_by_3):
      print(  "%d fizz." )   
elif(divided_by_7):
      print("%d buzz." )
else:
      print("The number %d is not divded neither by 3 or 7 " % num)

#correct way
num = 21
if num%3==0:
    print("fizz")
elif num%7==0:
    print("buzz")
elif num%3==0  and num%7==0:
    print("fizzbuzz")      

# if num%3==0 and num%7==0:
     #print("fizzbuzz")
 #elif num%3==0:
 #    print("fizz")
 # elfi num%7==0:
 #    print("buzz")
 # else:
 #     print(num)
 #    


