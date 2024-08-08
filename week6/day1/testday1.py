# List of names on the guest list
guest_list = [
    "Johny" ,
    "Billy",
    "Sam",
    "Cruella",
    "Sophie",
    "Naty",
    "Bob"
    ]

# List of names on the barred list
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
        print(f"{name}, you are on the guest list. You can enter.")
    elif name in barred_list:
        print(f"{name}, you are on the barred list. You can`t come in.")
    else:
        print(f"{name}, you are not on the guest list. You must wait.")


def main():
    while True:
        name = input("Please tell me your name  ")

        check_guest(name)


main()
