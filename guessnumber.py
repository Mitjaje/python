number = 3
inputnumber = 0

while number != inputnumber :
    inputnumber = input("Please try to guesss a number between 0 and 10: ")
    if inputnumber <= 10 and inputnumber >= 0 :
        if inputnumber < number :
            print("Try higher!")
        elif inputnumber > number :
            print("Try lower!")
    else :
        print("Stay between 0 and 10!")
print("Bingo!")

