from collections import deque
calculations = deque()

for item in range(0, 5):
    get_item = input("Enter an Item: ")

    calculations.appenedleft(get_item)


print()
print("*** The Entire Deque ***")
print(calculations)

print()

print("*** The 3 Most Recent ***")
for item in range(0, 3):
    print(calculations[item])


