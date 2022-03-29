data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

filename = input("Enter a Filename: ")

filename = filename + ".txt"

f = open(filename, "W+")

for item in data:
    f.write(item + "/n")

f.close()
