# TODO

def main():
    # user prompt function
    owned = get_owned()

    quarters = calculate_quarters(owned)
    # caluculate remaining owned
    owned = owned - quarters * 0.25

    dimes = calculate_dimes(owned)
    owned = owned - dimes * 0.10

    nickels = calculate_nickels(owned)
    owned = owned - nickels * 0.05

    pennies = calculate_pennies(owned)
    owned = owned - pennies * 0.01

    coins = quarters + dimes + nickels + pennies

    print(f"{coins}")


def get_owned():
    while True:
        try:
            change_owed = float(input("Change owned: "))
            # checking conditions
            if change_owed > 0:
                return change_owed
        # if not float return get_owned()
        except ValueError:
            return get_owned()


def calculate_quarters(owned):
    q = 0
    while round(owned, 2) >= 0.25:
        owned = owned - 0.25
        q += 1
    # return quarters count
    return q


def calculate_dimes(owned):
    d = 0
    while round(owned, 2) >= 0.10:
        owned = owned - 0.10
        d += 1
    # return dimes count
    return d


def calculate_nickels(owned):
    n = 0
    while round(owned, 2) >= 0.05:
        owned = owned - 0.05
        n += 1
    # return nickels count
    return n


def calculate_pennies(owned):
    p = 0
    while round(owned, 2) >= 0.01:
        owned = owned - 0.01
        p += 1
    # return count pennies
    return p


main()