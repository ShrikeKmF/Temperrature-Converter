import re

data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

filename = input("Enter a Filename: ")

valid_file = "[A-Zaz]"

if re.match(valid_file, filename):
    filename = filename + ".txt"

    f = open(filename, "W+")

    for item in data:
        f.write(item + "/n")

    f.close()

else:
    print("oops")
