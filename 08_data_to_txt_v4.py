import re

has_error = "yes"
while has_error == "yes":
    print()
    filename = input("Enter a Filename: ")

    valid_char = "[A-Zaz]"
    for letter in filename:
        if re.match(valid_char, letter):
            continue

        elif letter == "  ":
            problem = "(No spaces allowed)"

        else:
            problem = "(no {}'s is allowed".format(letter)
        has_error = "yes"

    if filename == "":
        problem = "FIlename can't be blank"
        has_error = "yes"

    if has_error == "yes":
        print("Invalid Filename - {}".format(problem))
    else:
        print("You have entered a valid filename")




