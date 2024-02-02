class Coffee:

    def __init__(self, name, kind, strength, price):
        self.name = name
        self.kind = kind
        self.strength = strength
        self.price = price

    def DisplayInfo(self):
        print("Name: ", self.name)
        print("Kind: ", self.kind)
        print("Strength:", self.strength)
        print("Price: ", self.price)


def SameProducts(list_of_capsules):
    counter = 0
    manufacturer = list_of_capsules[0].kind
    for i in range(len(list_of_capsules)):
        if manufacturer == list_of_capsules[i].kind:
            continue
        else:
            counter += 1
    if counter == 0:
        return True
    else:
        return False


capsule1 = Coffee("Cappuccino", "Espresso", 19, 3.5)
capsule2 = Coffee("Cappuccino", "Esp1re3sso", 1, 8)
capsule3 = Coffee("Cappuccino", "Espresso", 5, 5)

# capsule1.DisplayInfo()
# capsule2.DisplayInfo()
# capsule3.DisplayInfo()

print(SameProducts([capsule1, capsule2, capsule3]))
