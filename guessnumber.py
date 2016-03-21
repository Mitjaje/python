number = 3
inputnumber = 0
error = 0

while number != int(inputnumber) :

    inputnumber = raw_input("\nPlease try to guesss a number between 0 and 10: ")
    try:
        val = int(inputnumber)
    except ValueError:
        print("\nOops, %s is not a number.." % inputnumber)
        error = 1
        break
    if int(inputnumber) <= 10 and int(inputnumber) >= 0 :
        if int(inputnumber) < number :
            print("\nTry higher!")
        elif int(inputnumber) > number :
            print("\nTry lower!")
    else :
        print(" \nIsn't between 0 and 10 hard enough??")
if error == 1 :
    error = 1
else :
    print("\n Bingo!")

