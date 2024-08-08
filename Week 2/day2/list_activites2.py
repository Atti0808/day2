#storing a lots of info in one place
#can contain many types of data types
# coffe_order = [
#     "Alex - Flat White",
#     "Izzy - Cappucino",
#     "Attila - Americano"

# ]
# print(coffe_order)

#list Syntax 
# list are stored in [] brackets

#each item in this case is a string - they will all need their own set of quation marks. 
#
#it can be done in the same line 
#when using a list each item should fit on it`s own line
# easier to read
car_parts = [
    "tyres - Front Tyres",
    "lights - front right bulb ",
    "service - oil change"
]

# print(car_parts)
# # car_parts[2]  = "service - screenwash topup " # start couting from 0 [-1] get`s last item entered`
# # print(len(car_parts[0])) # used indexing
# print(car_parts[2][-1])

#index in Lists

#acces individual items.
# we access them by the []
# '

#we can use len() - showing all items and how many and not starting from 0



#.append add another item to the list to the end of our list

car_parts.append("windows - windshield replacement")
print(car_parts)


#.pop - removes item from the list


car_parts.pop()
print(car_parts)


#.pop can also remove an specific item from the list

car_parts.pop(1)

print(car_parts) # counting starts from 0
