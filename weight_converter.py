weight = input("Weight: ")
weight2 = input("(L)bs OR (K)g: ")
if weight2.upper() == "L":
    conv = (int(weight) * 0.45)
    print(f"You are {conv} kilograms")

elif weight2.upper() == "K":
    conv = (int(weight) / 0.45)
    print(f"You are {conv} pounds")
