data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

filename = input("Enter a Filename: ")

f = open(filename, "W+")

for item in data:
    f.write(item)

f.close()
