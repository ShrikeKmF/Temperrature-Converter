all_calculations = []

for item in range(0, 5):
    get_item = input("Enter an Item: ")
    all_calculations.append(get_item)

all_calculations.reverse()

print()
print("*** The Full List ***")
print(all_calculations)

print()

print("*** The 3 Most Recent ***")
for item in range(0, 3):
    print(all_calculations[len(all_calculations) - item - 1])


