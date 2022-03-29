all_calculations = []

get_item= ""
while get_item != 22:
    get_item = input("Enter an Item: ")

    if get_item == "zz":
        break

    all_calculations.append(get_item)


print()

if len(all_calculations) == 0:
    print("Oops - The list is empty")

else:
    print()
    print("*** The Full List ***")
    print(all_calculations)

    if len(all_calculations) >= 3:
        print("*** The Last 3 ***")
        for item in range(0, 3):
            print(all_calculations[len(all_calculations) - item - 1])

    else:
        print("**** Items from Newest to Oldest ****")
        for item in all_calculations:
            print(all_calculations[len(all_calculations) -
                                   all_calculations.index(item) - 1])

