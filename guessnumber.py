number = 3
inputnumber = 0

while number != int(inputnumber):

    inputnumber = raw_input("\nPlease try to guesss a number between 0 and 10: ")
    try:
        value = int(inputnumber)
    except ValueError:
        print("\nOops, %s is not a number.." % inputnumber)
        break
    if value <= 10 and value >= 0:
        if value < number:
            print("\nTry higher!")
        elif value > number:
            print("\nTry lower!")
        elif value == number:
            print("\n Bingo!")
    else:
        print(" \nIsn't between 0 and 10 hard enough??")
