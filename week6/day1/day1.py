print("Type in tow numbers to multiply them")




while True:
    try:
        num1 = int(input(">>"))
        num2 = int(input(">>"))
        break
    except ValueError:
        print("Please try again using numbers only")

print (num1*num2)
