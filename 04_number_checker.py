def temp_check(low):
    valid = False
    while not valid:
        try:
            response = float(input("Enter a number: "))
            if response < low:
                print("To Cold!")
            else:
                return response

        except ValueError:
            print("Please enter a number: ")


number = temp_check(-273)
print("You entered {}".format(number))

number = temp_check(-459)
print("You entered {}".format(number))
