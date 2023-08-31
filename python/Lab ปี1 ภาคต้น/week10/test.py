menu = {
    "drink": ["Coke", "Milk", "Tea", "Water"],
    "price": {1: 20, 2: 15, 3: 20, 4: 10},
}
drink , price = menu.values()
print("Menu")
for key in range(1 , price.__len__() + 1):
    print(f"{key}.\t {drink[key - 1]} {price[key]} bath")

_continue = "y"
order = 0
while True:
    amount = 0
    order += 1
    print(f"\nOrder#{order}")
    while True:
        item = int(input("Item : "))
        if item == 0 or item not in list(price.keys()):
            print(f"Amount: {amount} bath")
            _continue = input("Continue (y/n) : ")
            isContinue = _continue == "y" or _continue.upper() == "y".upper()
            if isContinue: break
            elif not isContinue: break
        else: amount += price[item]
    if not isContinue: break