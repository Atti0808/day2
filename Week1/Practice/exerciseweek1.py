# name = "Natalia"
# print(len(name))
# print(name.find("a"))
# print(name.capitalize())
# print(name.lower())
#print(name.count("a"))
#print(name.replace("a","e"))
#print(name*2)
#print(name.strip("a"))
# username = input("please input your name ")
# print(f"Hello {username}")
# fav_colour = input("What is your favourite colour?")
# print(f"{fav_colour} really ? That is my favourite colour")
# your_age = input("Please tell us your age ")
# print(f"{your_age}? , Thank you")
# apples =(0.25)
# ammount = input("How many apples would you like?")
# print(apples*ammount)
# first_name = input("Please enter your first name : ")
# last_name = input("Please enter your last name :  ")
# print("Hello, "  + first_name.capitalize() +  ' '  + last_name.capitalize() )
# first_name = "Attila"
# last_name = "Kilin"
# output = "Hello , {1} {0}".format (first_name , last_name)
# output = "hello "  + first_name + ' '  + last_name
# output =f"Hello , {first_name} {last_name}"
# print(output) 
# first_num = 0.25
# second_num = 6
# print(first_num * second_num)
# days_in_feb = 28
# print (str ( days_in_feb) + " days in February
# first_num = input("How many apples")
# apples = 0.25
# print(int(first_num ) * float(apples))
# apples = 0.25
# print(apples)
# first_num =  input("how many do you want ?")
# second_num = input("how many would you like ?")
# print(int(first_num) + int(second_num))
# days_in_February = 28
# print(str(days_in_February) + " total days in February ")

# from datetime import datetime, timedelta


# # current_date = datetime.now()
# # print("Today is " + str(current_date))


# today = datetime.now()
# print("Todays is" + str(today))
# one_day = timedelta(day =1)
# yesterday = today - one_day
# print("Yesterday was" + str(yesterday))

# from datetime import datetime
# birthday = input("When is your Birthday(dd/mm/yyyy)")

# birthday_date = datetime.strptime(birthday ,"%d/%m/%Y")

# print("Birthday : " + str(birthday_date))
from datetime import datetime , timedelta

# today = datetime.now()

# one_day = timedelta(day=1)
# yesterday = today - one_day

# print("Yesterday was : " str(yesterday))
today = datetime.now()
# one_week = timedelta(weeks=1)
# last_week = today - one_week
# print("last week was : " + str(last_week))

print("Day " + str(today.day))
