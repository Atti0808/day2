#create two list of name ; a guest list and barred list.
#create a function which takes a guest`s name.
#if the name appears on the guest list , let the user know they can enter.#
#if the name doesn`t appear on the guest list , let the user know they must wait.
# if the name appears on the barred list , the gues must turned away.

name = input("Please enter name here:")

guest_list = [
     "Johny" ,
    "Billy",
    "Sam",
    "Cruella",
    "Sophie",
    "Naty",
    "Bob"
]

barred_list = [
    "Tom",
    "Mac",
    "Joe",
    "Suzie",
    "James",
    "Joey",
    "Izabella"
]

def check_guest(name):
    if name in guest_list:
        print(f"{name}, thank you for coming tonight.")
    elif name in barred_list:
        print(f"{name}, Sorry you will not be able to attend tonight!")
    else:
        print(f"{name} , sorry you are not on the guest list. You must wait")


   



